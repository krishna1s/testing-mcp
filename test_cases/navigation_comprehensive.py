"""
Navigation and UI Comprehensive Tests - Playwright Website
========================================================

Comprehensive testing of navigation patterns, UI elements, and user interface interactions
discovered through analysis of the TypeScript recording and comprehensive exploration:

1. Main navigation menu testing
2. Page transitions and loading states
3. UI element interactions (buttons, links, dropdowns)
4. Responsive behavior testing
5. Dynamic content and loading scenarios
6. Error page handling and recovery
"""

import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_main_navigation_elements(playwright: Playwright) -> None:
    """
    Test main navigation elements and menu interactions
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    
    try:
        print("🧭 Testing main navigation elements...")
        
        page.goto("https://playwright.microsoft.com/", wait_until="networkidle")
        page.screenshot(path=f"nav_01_main_page_{int(time.time())}.png")
        
        # Test main navigation links and buttons
        navigation_elements = [
            {"type": "button", "name": "Sign in"},
            {"type": "link", "name": "Docs"},
            {"type": "link", "name": "API"},
            {"type": "link", "name": "Community"},
        ]
        
        for i, element in enumerate(navigation_elements):
            try:
                if element["type"] == "button":
                    nav_element = page.get_by_role("button", name=element["name"])
                else:
                    nav_element = page.get_by_role("link", name=element["name"])
                
                if nav_element.is_visible():
                    print(f"✅ Found navigation element: {element['name']}")
                    
                    # Test hover behavior
                    nav_element.hover()
                    page.wait_for_timeout(500)
                    page.screenshot(path=f"nav_02_hover_{element['name']}_{int(time.time())}.png")
                    
                    # For non-sign-in elements, test click behavior
                    if element["name"] != "Sign in":
                        try:
                            nav_element.click()
                            page.wait_for_load_state("networkidle")
                            page.screenshot(path=f"nav_03_clicked_{element['name']}_{int(time.time())}.png")
                            
                            # Navigate back to main page
                            page.go_back()
                            page.wait_for_load_state("networkidle")
                        except Exception as e:
                            print(f"⚠️ Navigation click failed for {element['name']}: {e}")
                    
                else:
                    print(f"⚠️ Navigation element not visible: {element['name']}")
                    
            except Exception as e:
                print(f"⚠️ Navigation element test failed for {element['name']}: {e}")
        
        print("✅ Main navigation elements test completed!")
        
    except Exception as e:
        print(f"❌ Main navigation elements test failed: {e}")
        page.screenshot(path=f"nav_failure_main_{int(time.time())}.png")
        raise
    finally:
        context.close()
        browser.close()


def test_page_transitions_and_loading(playwright: Playwright) -> None:
    """
    Test page transitions, loading states, and navigation flows
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    
    try:
        print("🔄 Testing page transitions and loading states...")
        
        # Test initial page load
        page.goto("https://playwright.microsoft.com/", wait_until="domcontentloaded")
        page.screenshot(path=f"nav_04_initial_load_{int(time.time())}.png")
        
        # Wait for full network idle
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"nav_05_network_idle_{int(time.time())}.png")
        
        # Test Sign in flow transition
        print("🔐 Testing sign in flow transitions...")
        sign_in_button = page.get_by_role("button", name="Sign in")
        expect(sign_in_button).to_be_visible()
        
        sign_in_button.click()
        
        # Monitor loading state during transition
        page.wait_for_load_state("domcontentloaded")
        page.screenshot(path=f"nav_06_signin_transition_{int(time.time())}.png")
        
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"nav_07_signin_loaded_{int(time.time())}.png")
        
        # Test form progression loading states
        email_field = page.get_by_role("textbox", name="Enter your email, phone, or")
        email_field.fill("pwtest@puneet0288hotmail.onmicrosoft.com")
        
        next_button = page.get_by_role("button", name="Next")
        next_button.click()
        
        # Monitor transition to password page
        page.wait_for_load_state("domcontentloaded")
        page.screenshot(path=f"nav_08_password_transition_{int(time.time())}.png")
        
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"nav_09_password_loaded_{int(time.time())}.png")
        
        print("✅ Page transitions and loading test completed!")
        
    except Exception as e:
        print(f"❌ Page transitions and loading test failed: {e}")
        page.screenshot(path=f"nav_failure_transitions_{int(time.time())}.png")
        raise
    finally:
        context.close()
        browser.close()


def test_responsive_behavior_and_viewports(playwright: Playwright) -> None:
    """
    Test responsive behavior across different viewport sizes
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    
    # Test different viewport sizes
    viewports = [
        {"name": "Desktop", "width": 1920, "height": 1080},
        {"name": "Tablet", "width": 768, "height": 1024},
        {"name": "Mobile", "width": 375, "height": 667},
        {"name": "Large Desktop", "width": 2560, "height": 1440},
    ]
    
    for viewport in viewports:
        context = browser.new_context(viewport={"width": viewport["width"], "height": viewport["height"]})
        page = context.new_page()
        
        try:
            print(f"📱 Testing {viewport['name']} viewport ({viewport['width']}x{viewport['height']})...")
            
            page.goto("https://playwright.microsoft.com/", wait_until="networkidle")
            page.screenshot(path=f"nav_10_{viewport['name']}_main_{int(time.time())}.png")
            
            # Test Sign in button visibility and position
            try:
                sign_in_button = page.get_by_role("button", name="Sign in")
                if sign_in_button.is_visible():
                    print(f"✅ Sign in button visible on {viewport['name']}")
                    
                    # Get button position for responsive analysis
                    bbox = sign_in_button.bounding_box()
                    if bbox:
                        print(f"📊 Sign in button position on {viewport['name']}: x={bbox['x']}, y={bbox['y']}")
                else:
                    print(f"⚠️ Sign in button not visible on {viewport['name']}")
            except Exception as e:
                print(f"⚠️ Sign in button test failed on {viewport['name']}: {e}")
            
            # Test navigation menu behavior on different screen sizes
            try:
                # Look for mobile menu indicators (hamburger menu, etc.)
                mobile_menu_selectors = [
                    "button[aria-label*='menu']",
                    "button[aria-label*='Menu']",
                    ".hamburger",
                    "[data-testid*='menu']"
                ]
                
                for selector in mobile_menu_selectors:
                    elements = page.locator(selector).all()
                    if elements:
                        print(f"🍔 Found potential mobile menu elements on {viewport['name']}: {len(elements)}")
                        break
                
            except Exception as e:
                print(f"⚠️ Mobile menu detection failed on {viewport['name']}: {e}")
            
            print(f"✅ {viewport['name']} viewport test completed!")
            
        except Exception as e:
            print(f"❌ {viewport['name']} viewport test failed: {e}")
            page.screenshot(path=f"nav_failure_{viewport['name']}_{int(time.time())}.png")
        finally:
            context.close()
    
    browser.close()
    print("✅ Responsive behavior test completed!")


def test_dynamic_content_and_interactions(playwright: Playwright) -> None:
    """
    Test dynamic content loading and interactive elements
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    
    try:
        print("⚡ Testing dynamic content and interactions...")
        
        page.goto("https://playwright.microsoft.com/", wait_until="networkidle")
        page.screenshot(path=f"nav_11_dynamic_start_{int(time.time())}.png")
        
        # Test hover interactions on various elements
        interactive_elements = page.locator("button, a, [role='button'], [role='link']").all()
        
        print(f"🎯 Found {len(interactive_elements)} interactive elements")
        
        for i, element in enumerate(interactive_elements[:10]):  # Test first 10 elements
            try:
                if element.is_visible():
                    element.hover()
                    page.wait_for_timeout(300)
                    
                    # Check for any dynamic changes (tooltips, color changes, etc.)
                    page.screenshot(path=f"nav_12_hover_element_{i}_{int(time.time())}.png")
                    
            except Exception as e:
                print(f"⚠️ Hover test failed for element {i}: {e}")
        
        # Test keyboard navigation
        print("⌨️ Testing keyboard navigation...")
        page.keyboard.press("Tab")
        page.wait_for_timeout(300)
        page.screenshot(path=f"nav_13_keyboard_nav_1_{int(time.time())}.png")
        
        page.keyboard.press("Tab")
        page.wait_for_timeout(300)
        page.screenshot(path=f"nav_14_keyboard_nav_2_{int(time.time())}.png")
        
        # Test scrolling behavior
        print("📜 Testing scrolling behavior...")
        page.evaluate("window.scrollTo(0, document.body.scrollHeight / 2)")
        page.wait_for_timeout(500)
        page.screenshot(path=f"nav_15_scroll_middle_{int(time.time())}.png")
        
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(500)
        page.screenshot(path=f"nav_16_scroll_bottom_{int(time.time())}.png")
        
        page.evaluate("window.scrollTo(0, 0)")
        page.wait_for_timeout(500)
        page.screenshot(path=f"nav_17_scroll_top_{int(time.time())}.png")
        
        print("✅ Dynamic content and interactions test completed!")
        
    except Exception as e:
        print(f"❌ Dynamic content and interactions test failed: {e}")
        page.screenshot(path=f"nav_failure_dynamic_{int(time.time())}.png")
        raise
    finally:
        context.close()
        browser.close()


def test_error_scenarios_and_recovery(playwright: Playwright) -> None:
    """
    Test error scenarios, 404 pages, and recovery mechanisms
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    
    try:
        print("🚨 Testing error scenarios and recovery...")
        
        # Test 404 page
        try:
            page.goto("https://playwright.microsoft.com/nonexistent-page", wait_until="domcontentloaded")
            page.wait_for_timeout(3000)
            page.screenshot(path=f"nav_18_404_page_{int(time.time())}.png")
            print("📄 404 page test completed")
        except Exception as e:
            print(f"⚠️ 404 page test issues: {e}")
        
        # Test navigation to valid page from error
        try:
            page.goto("https://playwright.microsoft.com/", wait_until="networkidle")
            page.screenshot(path=f"nav_19_recovery_main_{int(time.time())}.png")
            print("🔄 Recovery to main page successful")
        except Exception as e:
            print(f"⚠️ Recovery navigation failed: {e}")
        
        # Test network error simulation (if possible)
        try:
            # Simulate slow network
            context.route("**/*", lambda route: route.continue_() if route.request.url.startswith("https://playwright.microsoft.com") else route.abort())
            page.reload()
            page.wait_for_timeout(3000)
            page.screenshot(path=f"nav_20_network_simulation_{int(time.time())}.png")
        except Exception as e:
            print(f"⚠️ Network simulation test: {e}")
        
        print("✅ Error scenarios and recovery test completed!")
        
    except Exception as e:
        print(f"❌ Error scenarios and recovery test failed: {e}")
        page.screenshot(path=f"nav_failure_error_scenarios_{int(time.time())}.png")
        raise
    finally:
        context.close()
        browser.close()


def test_accessibility_and_keyboard_navigation(playwright: Playwright) -> None:
    """
    Test accessibility features and keyboard navigation patterns
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    
    try:
        print("♿ Testing accessibility and keyboard navigation...")
        
        page.goto("https://playwright.microsoft.com/", wait_until="networkidle")
        page.screenshot(path=f"nav_21_accessibility_start_{int(time.time())}.png")
        
        # Test tab navigation through main elements
        tab_sequence = []
        for i in range(10):  # Test first 10 tab stops
            page.keyboard.press("Tab")
            page.wait_for_timeout(300)
            
            # Try to identify the focused element
            focused_element = page.evaluate("document.activeElement.tagName + (document.activeElement.textContent ? ': ' + document.activeElement.textContent.substring(0, 20) : '')")
            tab_sequence.append(focused_element)
            page.screenshot(path=f"nav_22_tab_{i+1}_{int(time.time())}.png")
        
        print(f"⌨️ Tab sequence: {tab_sequence}")
        
        # Test Enter key activation
        try:
            page.keyboard.press("Enter")
            page.wait_for_timeout(1000)
            page.screenshot(path=f"nav_23_enter_activation_{int(time.time())}.png")
        except Exception as e:
            print(f"⚠️ Enter key activation: {e}")
        
        # Test Escape key (should cancel any opened dialogs)
        try:
            page.keyboard.press("Escape")
            page.wait_for_timeout(500)
            page.screenshot(path=f"nav_24_escape_key_{int(time.time())}.png")
        except Exception as e:
            print(f"⚠️ Escape key test: {e}")
        
        print("✅ Accessibility and keyboard navigation test completed!")
        
    except Exception as e:
        print(f"❌ Accessibility and keyboard navigation test failed: {e}")
        page.screenshot(path=f"nav_failure_accessibility_{int(time.time())}.png")
        raise
    finally:
        context.close()
        browser.close()


def run_all_navigation_tests(playwright: Playwright) -> None:
    """
    Run all navigation and UI tests in sequence
    """
    print("🚀 Starting comprehensive navigation and UI tests...")
    
    tests = [
        ("Main Navigation Elements", test_main_navigation_elements),
        ("Page Transitions and Loading", test_page_transitions_and_loading),
        ("Responsive Behavior and Viewports", test_responsive_behavior_and_viewports),
        ("Dynamic Content and Interactions", test_dynamic_content_and_interactions),
        ("Error Scenarios and Recovery", test_error_scenarios_and_recovery),
        ("Accessibility and Keyboard Navigation", test_accessibility_and_keyboard_navigation),
    ]
    
    for test_name, test_func in tests:
        try:
            test_func(playwright)
            print(f"✅ {test_name}: PASSED")
        except Exception as e:
            print(f"❌ {test_name}: FAILED - {e}")
    
    print("🎉 Navigation and UI tests completed!")


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run_all_navigation_tests(playwright)