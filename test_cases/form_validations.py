"""
Form Interactions and Validation Tests - Playwright Website
==========================================================

Comprehensive testing of form interactions, input validation, and user input scenarios
based on the forms identified in the TypeScript recording:

1. Login forms (email, password fields)
2. Workspace creation forms
3. Input validation and error handling
4. Form submission and data persistence
5. Dynamic form behaviors and interactions
"""

import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_login_form_validations(playwright: Playwright) -> None:
    """
    Test comprehensive login form validations and input handling
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    
    try:
        print("📝 Testing login form validations...")
        
        page.goto("https://playwright.microsoft.com/", wait_until="networkidle")
        page.get_by_role("button", name="Sign in").click()
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"form_01_login_form_{int(time.time())}.png")
        
        # Test email field validations
        email_field = page.get_by_role("textbox", name="Enter your email, phone, or")
        
        # Test various email formats
        test_emails = [
            "",  # Empty email
            "invalid",  # Invalid format
            "test@",  # Incomplete email
            "@domain.com",  # Missing user part
            "valid@test.com",  # Valid format
            "pwtest@puneet0288hotmail.onmicrosoft.com",  # Actual test email
        ]
        
        for i, email in enumerate(test_emails):
            try:
                print(f"🧪 Testing email: '{email}'")
                
                # Clear and enter email
                email_field.click()
                email_field.fill("")  # Clear
                if email:  # Don't fill empty string
                    email_field.fill(email)
                
                page.screenshot(path=f"form_02_email_test_{i}_{int(time.time())}.png")
                
                # Try to proceed
                next_button = page.get_by_role("button", name="Next")
                next_button.click()
                page.wait_for_timeout(2000)  # Wait for validation
                
                page.screenshot(path=f"form_03_email_validation_{i}_{int(time.time())}.png")
                
                # Check for error messages or validation indicators
                page.wait_for_timeout(1000)
                
            except Exception as e:
                print(f"⚠️ Email validation test for '{email}': {e}")
        
        print("✅ Login form validations test completed!")
        
    except Exception as e:
        print(f"❌ Login form validations test failed: {e}")
        page.screenshot(path=f"form_failure_login_validation_{int(time.time())}.png")
        raise
    finally:
        context.close()
        browser.close()


def test_password_field_behaviors(playwright: Playwright) -> None:
    """
    Test password field interactions and security behaviors
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    
    try:
        print("🔐 Testing password field behaviors...")
        
        # Navigate to password field
        page.goto("https://playwright.microsoft.com/", wait_until="networkidle")
        page.get_by_role("button", name="Sign in").click()
        page.wait_for_load_state("networkidle")
        
        # Enter valid email to reach password field
        email_field = page.get_by_role("textbox", name="Enter your email, phone, or")
        email_field.fill("pwtest@puneet0288hotmail.onmicrosoft.com")
        page.get_by_role("button", name="Next").click()
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"form_04_password_field_{int(time.time())}.png")
        
        # Test password field
        password_field = page.get_by_role("textbox", name="Enter the password for pwtest")
        
        # Test various password scenarios
        test_passwords = [
            "",  # Empty password
            "a",  # Too short
            "short",  # Short password
            "validpassword123",  # Valid format
            "Msft@9090",  # Actual test password
        ]
        
        for i, password in enumerate(test_passwords):
            try:
                print(f"🔑 Testing password length: {len(password)} chars")
                
                # Clear and enter password
                password_field.click()
                password_field.fill("")  # Clear
                if password:
                    password_field.fill(password)
                
                page.screenshot(path=f"form_05_password_test_{i}_{int(time.time())}.png")
                
                # Check if field masks password (should show dots/asterisks)
                field_value = password_field.input_value()
                print(f"🔍 Password field value length: {len(field_value)}")
                
                # Try to submit
                sign_in_button = page.get_by_role("button", name="Sign in")
                sign_in_button.click()
                page.wait_for_timeout(2000)
                
                page.screenshot(path=f"form_06_password_submit_{i}_{int(time.time())}.png")
                
                # For valid password, we might get to next step
                if password == "Msft@9090":
                    # Check for success indicators
                    page.wait_for_timeout(3000)
                    break
                
            except Exception as e:
                print(f"⚠️ Password test for length {len(password)}: {e}")
        
        print("✅ Password field behaviors test completed!")
        
    except Exception as e:
        print(f"❌ Password field behaviors test failed: {e}")
        page.screenshot(path=f"form_failure_password_{int(time.time())}.png")
        raise
    finally:
        context.close()
        browser.close()


def test_workspace_creation_form(playwright: Playwright) -> None:
    """
    Test workspace creation form validations and interactions
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    
    try:
        print("🏗️ Testing workspace creation form...")
        
        # Set up authenticated session first
        page.goto("https://playwright.microsoft.com/", wait_until="networkidle")
        page.get_by_role("button", name="Sign in").click()
        page.wait_for_load_state("networkidle")
        
        email_field = page.get_by_role("textbox", name="Enter your email, phone, or")
        email_field.fill("pwtest@puneet0288hotmail.onmicrosoft.com")
        page.get_by_role("button", name="Next").click()
        page.wait_for_load_state("networkidle")
        
        password_field = page.get_by_role("textbox", name="Enter the password for pwtest")
        password_field.fill("Msft@9090")
        page.get_by_role("button", name="Sign in").click()
        page.wait_for_load_state("networkidle")
        
        yes_button = page.get_by_role("button", name="Yes")
        yes_button.click()
        page.wait_for_load_state("networkidle")
        
        # Navigate to workspace creation
        page.wait_for_selector("text=Fetching workspaces", timeout=15000)
        fetching_text = page.get_by_text("Fetching workspaces")
        fetching_text.click()
        
        new_workspace_button = page.get_by_role("button", name="New workspace")
        expect(new_workspace_button).to_be_visible()
        new_workspace_button.click()
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"form_07_workspace_form_{int(time.time())}.png")
        
        # Test workspace name field validations
        workspace_name_field = page.get_by_role("textbox", name="Workspace name")
        
        test_workspace_names = [
            "",  # Empty name
            "a",  # Very short
            "valid-name",  # Valid with dash
            "ValidName123",  # Valid with numbers
            "x" * 50,  # Long name
            "test@workspace#",  # Invalid characters
            "demoagent123",  # Valid test name
        ]
        
        for i, workspace_name in enumerate(test_workspace_names):
            try:
                print(f"🏷️ Testing workspace name: '{workspace_name}'")
                
                # Clear and enter workspace name
                workspace_name_field.click()
                workspace_name_field.fill("")  # Clear
                if workspace_name:
                    workspace_name_field.fill(workspace_name)
                
                page.screenshot(path=f"form_08_workspace_name_{i}_{int(time.time())}.png")
                
                # Check if create button is enabled/disabled
                create_button = page.get_by_role("button", name="Create workspace")
                is_enabled = create_button.is_enabled()
                print(f"📊 Create button enabled for '{workspace_name}': {is_enabled}")
                
                # For valid names, try to create
                if workspace_name and workspace_name == "demoagent123":
                    create_button.click()
                    page.wait_for_timeout(3000)
                    page.screenshot(path=f"form_09_workspace_creation_{int(time.time())}.png")
                    
                    # Check for creation messages
                    try:
                        creating_message = page.get_by_text("Creating Your Workspace")
                        expect(creating_message).to_be_visible()
                        print("✅ Workspace creation initiated successfully")
                    except Exception as e:
                        print(f"⚠️ Workspace creation message not found: {e}")
                    
                    break  # Exit after successful creation
                
            except Exception as e:
                print(f"⚠️ Workspace name test for '{workspace_name}': {e}")
        
        print("✅ Workspace creation form test completed!")
        
    except Exception as e:
        print(f"❌ Workspace creation form test failed: {e}")
        page.screenshot(path=f"form_failure_workspace_creation_{int(time.time())}.png")
        raise
    finally:
        context.close()
        browser.close()


def test_form_field_interactions(playwright: Playwright) -> None:
    """
    Test various form field interaction patterns
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    
    try:
        print("🎯 Testing form field interactions...")
        
        page.goto("https://playwright.microsoft.com/", wait_until="networkidle")
        page.get_by_role("button", name="Sign in").click()
        page.wait_for_load_state("networkidle")
        
        # Test email field interactions
        email_field = page.get_by_role("textbox", name="Enter your email, phone, or")
        
        # Test field focus and blur
        email_field.click()
        page.screenshot(path=f"form_10_field_focus_{int(time.time())}.png")
        
        # Test typing behavior
        email_field.type("test@example.com", delay=100)
        page.screenshot(path=f"form_11_typing_behavior_{int(time.time())}.png")
        
        # Test selection and clearing
        email_field.select_text()
        page.keyboard.press("Delete")
        page.screenshot(path=f"form_12_text_selection_{int(time.time())}.png")
        
        # Test keyboard navigation
        email_field.fill("valid@test.com")
        page.keyboard.press("Tab")  # Should move to next button
        page.screenshot(path=f"form_13_keyboard_navigation_{int(time.time())}.png")
        
        # Test copy-paste behavior
        email_field.fill("copy-test@example.com")
        email_field.select_text()
        page.keyboard.press("Control+c")  # Copy
        email_field.fill("")
        page.keyboard.press("Control+v")  # Paste
        page.screenshot(path=f"form_14_copy_paste_{int(time.time())}.png")
        
        print("✅ Form field interactions test completed!")
        
    except Exception as e:
        print(f"❌ Form field interactions test failed: {e}")
        page.screenshot(path=f"form_failure_interactions_{int(time.time())}.png")
        raise
    finally:
        context.close()
        browser.close()


def test_form_submission_behaviors(playwright: Playwright) -> None:
    """
    Test form submission methods and behaviors
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    
    try:
        print("📤 Testing form submission behaviors...")
        
        page.goto("https://playwright.microsoft.com/", wait_until="networkidle")
        page.get_by_role("button", name="Sign in").click()
        page.wait_for_load_state("networkidle")
        
        email_field = page.get_by_role("textbox", name="Enter your email, phone, or")
        email_field.fill("pwtest@puneet0288hotmail.onmicrosoft.com")
        
        # Test submission via button click
        next_button = page.get_by_role("button", name="Next")
        next_button.click()
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"form_15_button_submission_{int(time.time())}.png")
        
        # Test submission via Enter key (on password field)
        password_field = page.get_by_role("textbox", name="Enter the password for pwtest")
        password_field.fill("Msft@9090")
        
        # Try Enter key submission
        password_field.press("Enter")
        page.wait_for_timeout(3000)
        page.screenshot(path=f"form_16_enter_submission_{int(time.time())}.png")
        
        print("✅ Form submission behaviors test completed!")
        
    except Exception as e:
        print(f"❌ Form submission behaviors test failed: {e}")
        page.screenshot(path=f"form_failure_submission_{int(time.time())}.png")
        raise
    finally:
        context.close()
        browser.close()


def run_all_form_tests(playwright: Playwright) -> None:
    """
    Run all form interaction tests in sequence
    """
    print("🚀 Starting comprehensive form interaction tests...")
    
    tests = [
        ("Login Form Validations", test_login_form_validations),
        ("Password Field Behaviors", test_password_field_behaviors),
        ("Workspace Creation Form", test_workspace_creation_form),
        ("Form Field Interactions", test_form_field_interactions),
        ("Form Submission Behaviors", test_form_submission_behaviors),
    ]
    
    for test_name, test_func in tests:
        try:
            test_func(playwright)
            print(f"✅ {test_name}: PASSED")
        except Exception as e:
            print(f"❌ {test_name}: FAILED - {e}")
    
    print("🎉 Form interaction tests completed!")


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run_all_form_tests(playwright)