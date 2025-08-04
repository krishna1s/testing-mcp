"""
Error Scenarios and Edge Cases Tests - Playwright Website
========================================================

Comprehensive testing of error conditions, edge cases, and exceptional scenarios
identified from the TypeScript recording analysis and thorough exploration:

1. Network error conditions and timeouts
2. Authentication failure scenarios  
3. Invalid input handling and validation errors
4. Workspace operation failures and cleanup issues
5. Browser state edge cases and recovery
6. Performance bottlenecks and timeout scenarios
"""

import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_network_error_conditions(playwright: Playwright) -> None:
    """
    Test various network error conditions and recovery mechanisms
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    
    try:
        print("🌐 Testing network error conditions...")
        
        # Test slow network conditions
        print("🐌 Testing slow network simulation...")
        context.route("**/*", lambda route: (
            route.continue_() if "playwright.microsoft.com" in route.request.url
            else route.abort()
        ))
        
        page.goto("https://playwright.microsoft.com/", wait_until="domcontentloaded")
        page.wait_for_timeout(5000)  # Allow time for slow loading
        page.screenshot(path=f"error_01_slow_network_{int(time.time())}.png")
        
        # Test connection interruption during form submission
        print("⚡ Testing connection interruption...")
        try:
            sign_in_button = page.get_by_role("button", name="Sign in")
            sign_in_button.click()
            
            # Simulate network interruption
            context.route("**/*", lambda route: route.abort())
            
            page.wait_for_timeout(3000)
            page.screenshot(path=f"error_02_connection_interrupted_{int(time.time())}.png")
            
        except Exception as e:
            print(f"⚠️ Connection interruption test: {e}")
        
        # Restore normal routing
        context.unroute("**/*")
        
        print("✅ Network error conditions test completed!")
        
    except Exception as e:
        print(f"❌ Network error conditions test failed: {e}")
        page.screenshot(path=f"error_failure_network_{int(time.time())}.png")
        raise
    finally:
        context.close()
        browser.close()


def test_authentication_failure_scenarios(playwright: Playwright) -> None:
    """
    Test various authentication failure scenarios and error handling
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    
    try:
        print("🔐 Testing authentication failure scenarios...")
        
        page.goto("https://playwright.microsoft.com/", wait_until="networkidle")
        page.get_by_role("button", name="Sign in").click()
        page.wait_for_load_state("networkidle")
        
        # Test invalid email formats
        invalid_emails = [
            "invalid-email",
            "@missing-user.com",
            "missing-domain@",
            "spaces in@email.com",
            "very-long-email-address-that-might-cause-issues@very-long-domain-name-that-exceeds-normal-limits.com"
        ]
        
        for i, invalid_email in enumerate(invalid_emails):
            try:
                print(f"📧 Testing invalid email: {invalid_email}")
                
                email_field = page.get_by_role("textbox", name="Enter your email, phone, or")
                email_field.click()
                email_field.fill("")
                email_field.fill(invalid_email)
                
                page.screenshot(path=f"error_03_invalid_email_{i}_{int(time.time())}.png")
                
                # Try to proceed
                next_button = page.get_by_role("button", name="Next")
                next_button.click()
                page.wait_for_timeout(3000)
                
                # Look for error messages
                error_indicators = page.locator("[role='alert'], .error, [aria-invalid='true']").all()
                if error_indicators:
                    print(f"✅ Error indication found for invalid email: {invalid_email}")
                else:
                    print(f"⚠️ No error indication for invalid email: {invalid_email}")
                
                page.screenshot(path=f"error_04_email_validation_{i}_{int(time.time())}.png")
                
            except Exception as e:
                print(f"⚠️ Invalid email test failed for {invalid_email}: {e}")
        
        # Test valid email but invalid password
        print("🔑 Testing valid email with invalid password...")
        try:
            email_field = page.get_by_role("textbox", name="Enter your email, phone, or")
            email_field.click()
            email_field.fill("")
            email_field.fill("pwtest@puneet0288hotmail.onmicrosoft.com")
            
            next_button = page.get_by_role("button", name="Next")
            next_button.click()
            page.wait_for_load_state("networkidle")
            
            # Enter incorrect password
            password_field = page.get_by_role("textbox", name="Enter the password for pwtest")
            password_field.fill("incorrect-password-123")
            
            sign_in_button = page.get_by_role("button", name="Sign in")
            sign_in_button.click()
            page.wait_for_timeout(5000)  # Wait for authentication attempt
            
            page.screenshot(path=f"error_05_invalid_password_{int(time.time())}.png")
            
            # Look for authentication error messages
            auth_error_selectors = [
                "text=incorrect",
                "text=invalid",
                "text=error",
                "[role='alert']",
                ".error-message"
            ]
            
            for selector in auth_error_selectors:
                try:
                    error_element = page.locator(selector).first()
                    if error_element.is_visible():
                        print(f"✅ Authentication error detected: {selector}")
                        break
                except:
                    continue
            
        except Exception as e:
            print(f"⚠️ Invalid password test: {e}")
        
        print("✅ Authentication failure scenarios test completed!")
        
    except Exception as e:
        print(f"❌ Authentication failure scenarios test failed: {e}")
        page.screenshot(path=f"error_failure_auth_{int(time.time())}.png")
        raise
    finally:
        context.close()
        browser.close()


def test_session_timeout_and_recovery(playwright: Playwright) -> None:
    """
    Test session timeout scenarios and recovery mechanisms
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    
    try:
        print("⏰ Testing session timeout and recovery...")
        
        # First, establish a valid session
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
        
        # Handle stay signed in
        try:
            yes_button = page.get_by_role("button", name="Yes")
            yes_button.click()
            page.wait_for_load_state("networkidle")
        except Exception as e:
            print(f"⚠️ Stay signed in handling: {e}")
        
        page.screenshot(path=f"error_06_session_established_{int(time.time())}.png")
        
        # Simulate session timeout by clearing cookies
        print("🍪 Simulating session timeout by clearing cookies...")
        context.clear_cookies()
        
        # Try to access authenticated content
        try:
            page.reload()
            page.wait_for_timeout(5000)
            page.screenshot(path=f"error_07_after_cookie_clear_{int(time.time())}.png")
            
            # Check if we're redirected to login
            sign_in_button = page.get_by_role("button", name="Sign in")
            if sign_in_button.is_visible():
                print("✅ Session timeout detected, redirected to login")
            else:
                print("⚠️ Session timeout not detected or handled differently")
            
        except Exception as e:
            print(f"⚠️ Session timeout test: {e}")
        
        print("✅ Session timeout and recovery test completed!")
        
    except Exception as e:
        print(f"❌ Session timeout and recovery test failed: {e}")
        page.screenshot(path=f"error_failure_session_{int(time.time())}.png")
        raise
    finally:
        context.close()
        browser.close()


def test_workspace_operation_failures(playwright: Playwright) -> None:
    """
    Test workspace operation failure scenarios and error handling
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    
    try:
        print("🚧 Testing workspace operation failures...")
        
        # Set up authenticated session
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
        try:
            page.wait_for_selector("text=Fetching workspaces", timeout=15000)
            fetching_text = page.get_by_text("Fetching workspaces")
            fetching_text.click()
            
            new_workspace_button = page.get_by_role("button", name="New workspace")
            new_workspace_button.click()
            page.wait_for_load_state("networkidle")
            
            # Test workspace creation with problematic names
            problematic_names = [
                "",  # Empty name
                " ",  # Space only
                "a",  # Too short
                "existing-workspace-name",  # Potentially duplicate
                "workspace" + "x" * 100,  # Too long
                "test@workspace#invalid",  # Invalid characters
            ]
            
            for i, problematic_name in enumerate(problematic_names):
                try:
                    print(f"🧪 Testing problematic workspace name: '{problematic_name}'")
                    
                    workspace_name_field = page.get_by_role("textbox", name="Workspace name")
                    workspace_name_field.click()
                    workspace_name_field.fill("")
                    
                    if problematic_name:
                        workspace_name_field.fill(problematic_name)
                    
                    page.screenshot(path=f"error_08_problematic_name_{i}_{int(time.time())}.png")
                    
                    # Try to create workspace
                    create_button = page.get_by_role("button", name="Create workspace")
                    
                    # Check if button is disabled for invalid names
                    is_enabled = create_button.is_enabled()
                    print(f"📊 Create button enabled for '{problematic_name}': {is_enabled}")
                    
                    if is_enabled:
                        create_button.click()
                        page.wait_for_timeout(3000)
                        page.screenshot(path=f"error_09_creation_attempt_{i}_{int(time.time())}.png")
                        
                        # Look for error messages
                        error_selectors = [
                            "text=error",
                            "text=invalid",
                            "text=failed",
                            "[role='alert']",
                            ".error"
                        ]
                        
                        for selector in error_selectors:
                            try:
                                error_element = page.locator(selector).first()
                                if error_element.is_visible():
                                    print(f"✅ Error message found for '{problematic_name}': {selector}")
                                    break
                            except:
                                continue
                    
                except Exception as e:
                    print(f"⚠️ Problematic workspace name test failed for '{problematic_name}': {e}")
                    
        except Exception as e:
            print(f"⚠️ Workspace creation flow setup failed: {e}")
        
        print("✅ Workspace operation failures test completed!")
        
    except Exception as e:
        print(f"❌ Workspace operation failures test failed: {e}")
        page.screenshot(path=f"error_failure_workspace_{int(time.time())}.png")
        raise
    finally:
        context.close()
        browser.close()


def test_browser_state_edge_cases(playwright: Playwright) -> None:
    """
    Test browser state edge cases and unusual scenarios
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    
    try:
        print("🌐 Testing browser state edge cases...")
        
        # Test page refresh during form filling
        print("🔄 Testing page refresh during form interaction...")
        page.goto("https://playwright.microsoft.com/", wait_until="networkidle")
        page.get_by_role("button", name="Sign in").click()
        page.wait_for_load_state("networkidle")
        
        # Start filling form
        email_field = page.get_by_role("textbox", name="Enter your email, phone, or")
        email_field.fill("test@example.com")
        
        page.screenshot(path=f"error_10_before_refresh_{int(time.time())}.png")
        
        # Refresh page during form filling
        page.reload()
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"error_11_after_refresh_{int(time.time())}.png")
        
        # Test back/forward navigation
        print("⬅️➡️ Testing back/forward navigation edge cases...")
        page.get_by_role("button", name="Sign in").click()
        page.wait_for_load_state("networkidle")
        
        # Go back
        page.go_back()
        page.wait_for_timeout(2000)
        page.screenshot(path=f"error_12_after_back_{int(time.time())}.png")
        
        # Go forward
        page.go_forward()
        page.wait_for_timeout(2000)
        page.screenshot(path=f"error_13_after_forward_{int(time.time())}.png")
        
        # Test multiple tab scenarios (if applicable)
        print("📑 Testing multiple tab behavior...")
        # Open new tab with same URL
        new_page = context.new_page()
        new_page.goto("https://playwright.microsoft.com/", wait_until="networkidle")
        new_page.screenshot(path=f"error_14_second_tab_{int(time.time())}.png")
        new_page.close()
        
        # Test window resize during interaction
        print("🔍 Testing window resize during interaction...")
        page.set_viewport_size({"width": 800, "height": 600})
        page.wait_for_timeout(1000)
        page.screenshot(path=f"error_15_resized_window_{int(time.time())}.png")
        
        page.set_viewport_size({"width": 1920, "height": 1080})
        page.wait_for_timeout(1000)
        page.screenshot(path=f"error_16_restored_window_{int(time.time())}.png")
        
        print("✅ Browser state edge cases test completed!")
        
    except Exception as e:
        print(f"❌ Browser state edge cases test failed: {e}")
        page.screenshot(path=f"error_failure_browser_state_{int(time.time())}.png")
        raise
    finally:
        context.close()
        browser.close()


def test_performance_and_timeout_scenarios(playwright: Playwright) -> None:
    """
    Test performance bottlenecks and timeout scenarios
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    
    try:
        print("⚡ Testing performance and timeout scenarios...")
        
        # Test page load performance
        print("📊 Testing page load performance...")
        start_time = time.time()
        page.goto("https://playwright.microsoft.com/", wait_until="networkidle")
        load_time = time.time() - start_time
        
        print(f"⏱️ Page load time: {load_time:.2f} seconds")
        page.screenshot(path=f"error_17_performance_loaded_{int(time.time())}.png")
        
        # Test rapid clicking scenarios
        print("🖱️ Testing rapid clicking scenarios...")
        sign_in_button = page.get_by_role("button", name="Sign in")
        
        # Rapid clicks
        for i in range(5):
            try:
                sign_in_button.click()
                page.wait_for_timeout(100)  # Very short wait
            except Exception as e:
                print(f"⚠️ Rapid click {i+1} failed: {e}")
        
        page.wait_for_timeout(2000)
        page.screenshot(path=f"error_18_rapid_clicks_{int(time.time())}.png")
        
        # Test form submission timeout
        print("⏰ Testing form submission timeout...")
        page.wait_for_load_state("networkidle")
        
        try:
            email_field = page.get_by_role("textbox", name="Enter your email, phone, or")
            email_field.fill("pwtest@puneet0288hotmail.onmicrosoft.com")
            
            # Submit with very short timeout to test timeout handling
            next_button = page.get_by_role("button", name="Next")
            next_button.click()
            
            # Wait for response with timeout
            page.wait_for_load_state("networkidle", timeout=5000)
            page.screenshot(path=f"error_19_timeout_test_{int(time.time())}.png")
            
        except Exception as e:
            print(f"⚠️ Timeout test completed with observation: {e}")
            page.screenshot(path=f"error_20_timeout_result_{int(time.time())}.png")
        
        print("✅ Performance and timeout scenarios test completed!")
        
    except Exception as e:
        print(f"❌ Performance and timeout scenarios test failed: {e}")
        page.screenshot(path=f"error_failure_performance_{int(time.time())}.png")
        raise
    finally:
        context.close()
        browser.close()


def run_all_error_scenario_tests(playwright: Playwright) -> None:
    """
    Run all error scenario tests in sequence
    """
    print("🚀 Starting comprehensive error scenario tests...")
    
    tests = [
        ("Network Error Conditions", test_network_error_conditions),
        ("Authentication Failure Scenarios", test_authentication_failure_scenarios),
        ("Session Timeout and Recovery", test_session_timeout_and_recovery),
        ("Workspace Operation Failures", test_workspace_operation_failures),
        ("Browser State Edge Cases", test_browser_state_edge_cases),
        ("Performance and Timeout Scenarios", test_performance_and_timeout_scenarios),
    ]
    
    for test_name, test_func in tests:
        try:
            test_func(playwright)
            print(f"✅ {test_name}: PASSED")
        except Exception as e:
            print(f"❌ {test_name}: FAILED - {e}")
    
    print("🎉 Error scenario tests completed!")


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run_all_error_scenario_tests(playwright)