"""
Main User Journey Test - Playwright Website Workspace Management
=====================================================

This test replicates the exact user journey captured in the TypeScript recording:
1. Navigate to Playwright website
2. Sign in with test credentials  
3. Create a new workspace named 'demoagent123'
4. Navigate to workspace management
5. Delete the created workspace
6. Handle optional survey and sign out

Based on comprehensive analysis of the original TypeScript recording.
"""

import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    """
    Main user journey test execution with comprehensive error handling
    and detailed documentation of each step.
    """
    # Enhanced configuration for comprehensive testing
    browser = playwright.chromium.launch(
        headless=False,  # FORCE headed mode for visibility
        slow_mo=500,     # Add delays for observation
        timeout=60000    # Extended timeout for complex operations
    )
    
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},  # Full HD for complete view
        record_video_dir="./test_videos/",  # Record test execution
    )
    
    page = context.new_page()
    
    try:
        print("🚀 Starting main user journey test execution...")
        
        # Step 1: Navigate to Playwright website
        print("📍 Step 1: Navigating to Playwright website...")
        page.goto("https://playwright.microsoft.com/", wait_until="networkidle")
        page.wait_for_load_state("networkidle")
        
        # Take screenshot of initial state
        page.screenshot(path=f"01_initial_page_{int(time.time())}.png")
        
        # Step 2: Verify Sign in button is visible and click it
        print("🔐 Step 2: Looking for Sign in button...")
        sign_in_button = page.get_by_role("button", name="Sign in")
        expect(sign_in_button).to_be_visible()
        print("✅ Sign in button found and visible")
        
        sign_in_button.click()
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"02_after_sign_in_click_{int(time.time())}.png")
        
        # Step 3: Enter email/username
        print("📧 Step 3: Entering email credentials...")
        email_field = page.get_by_role("textbox", name="Enter your email, phone, or")
        email_field.click()
        email_field.fill("pwtest@puneet0288hotmail.onmicrosoft.com")
        
        # Click Next button
        next_button = page.get_by_role("button", name="Next")
        next_button.click()
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"03_after_email_entry_{int(time.time())}.png")
        
        # Step 4: Enter password
        print("🔑 Step 4: Entering password...")
        password_field = page.get_by_role("textbox", name="Enter the password for pwtest")
        password_field.click()
        password_field.fill("Msft@9090")
        
        # Click Sign in button
        sign_in_submit = page.get_by_role("button", name="Sign in")
        sign_in_submit.click()
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"04_after_password_entry_{int(time.time())}.png")
        
        # Step 5: Handle "Stay signed in?" dialog
        print("⚡ Step 5: Handling stay signed in dialog...")
        stay_signed_in_heading = page.get_by_role("heading", name="Stay signed in?")
        expect(stay_signed_in_heading).to_be_visible()
        
        yes_button = page.get_by_role("button", name="Yes")
        yes_button.click()
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"05_after_stay_signed_in_{int(time.time())}.png")
        
        # Step 6: Wait for workspace loading and click "New workspace"
        print("🏗️ Step 6: Waiting for workspace interface and creating new workspace...")
        
        # Wait for "Fetching workspaces" text and click it
        fetching_text = page.get_by_text("Fetching workspaces")
        fetching_text.click()
        
        # Wait for and verify "New workspace" button
        new_workspace_button = page.get_by_role("button", name="New workspace")
        expect(new_workspace_button).to_be_visible()
        print("✅ New workspace button found and visible")
        
        new_workspace_button.click()
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"06_after_new_workspace_click_{int(time.time())}.png")
        
        # Step 7: Enter workspace name
        print("📝 Step 7: Entering workspace name...")
        workspace_name_field = page.get_by_role("textbox", name="Workspace name")
        workspace_name_field.click()
        workspace_name_field.fill("demoagent123")
        
        # Click "Create workspace" button
        create_workspace_button = page.get_by_role("button", name="Create workspace")
        create_workspace_button.click()
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"07_after_workspace_creation_{int(time.time())}.png")
        
        # Step 8: Verify workspace creation messages
        print("⏳ Step 8: Verifying workspace creation process...")
        creating_message = page.get_by_text("Creating Your Workspace")
        expect(creating_message).to_be_visible()
        
        wait_message = page.get_by_text("This may take a few minutes.")
        expect(wait_message).to_be_visible()
        print("✅ Workspace creation messages verified")
        
        # Step 9: Navigate to the created workspace
        print("🎯 Step 9: Navigating to created workspace...")
        # Note: The URL will be dynamic based on actual workspace creation
        # This is a placeholder - in real execution, we'd extract the actual URL
        page.goto("https://playwright.microsoft.com/workspaces/westeurope_97ccc964-ac00-4a58-b243-ba0305b2f3a8")
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"08_workspace_page_{int(time.time())}.png")
        
        # Step 10: Verify workspace content
        print("🔍 Step 10: Verifying workspace content...")
        heading = page.get_by_role("heading", name="Run high-scale parallel tests").first()
        expect(heading).to_be_visible()
        
        # Step 11: Access workspace management
        print("⚙️ Step 11: Accessing workspace management...")
        workspace_button = page.get_by_role("button", name="demoagent123")
        workspace_button.click()
        
        manage_workspaces = page.get_by_text("Manage all workspaces")
        manage_workspaces.click()
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"09_workspace_management_{int(time.time())}.png")
        
        # Step 12: Verify workspace in management view
        print("👀 Step 12: Verifying workspace in management view...")
        html_element = page.locator("html")
        expect(html_element).to_be_visible()
        
        workspace_label = page.get_by_label("Workspace demoagent123").get_by_text("demoagent123")
        expect(workspace_label).to_be_visible()
        
        # Step 13: Delete workspace
        print("🗑️ Step 13: Deleting workspace...")
        manage_workspace_button = page.get_by_role("group", name="Workspace demoagent123").get_by_label("Manage workspace")
        manage_workspace_button.click()
        
        delete_workspace_text = page.get_by_text("Delete Workspace")
        delete_workspace_text.click()
        
        # Confirm deletion (first delete button)
        delete_button_1 = page.get_by_role("button", name="Delete")
        delete_button_1.click()
        
        # Confirm deletion (second delete button)
        delete_button_2 = page.get_by_role("button", name="Delete")
        delete_button_2.click()
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"10_after_workspace_deletion_{int(time.time())}.png")
        
        # Step 14: Verify deletion process
        print("✅ Step 14: Verifying workspace deletion...")
        deleting_message = page.get_by_text("Deleting workspace")
        expect(deleting_message).to_be_visible()
        
        # Step 15: Handle optional survey
        print("📋 Step 15: Handling optional survey...")
        survey_text = page.get_by_text("Optional Survey")
        expect(survey_text).to_be_visible()
        
        cancel_button = page.get_by_role("button", name="Cancel")
        cancel_button.click()
        page.screenshot(path=f"11_after_survey_cancel_{int(time.time())}.png")
        
        # Step 16: Additional navigation interactions
        print("🧭 Step 16: Performing additional navigation...")
        p_text_1 = page.get_by_text("P", exact=True)
        p_text_1.click()
        
        manage_workspace_text = page.get_by_text("Manage workspaceWorkspacesManage workspaces within your chosen")
        manage_workspace_text.click()
        
        # Step 17: Sign out
        print("👋 Step 17: Signing out...")
        p_text_2 = page.get_by_text("P", exact=True)
        p_text_2.click()
        
        sign_out_text = page.get_by_text("Sign Out")
        sign_out_text.click()
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"12_final_signed_out_{int(time.time())}.png")
        
        print("🎉 Main user journey test completed successfully!")
        
    except Exception as e:
        print(f"❌ Test failed with detailed error: {e}")
        # Take screenshot on failure for debugging
        page.screenshot(path=f"failure_main_journey_{int(time.time())}.png")
        raise
        
    finally:
        context.close()
        browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)