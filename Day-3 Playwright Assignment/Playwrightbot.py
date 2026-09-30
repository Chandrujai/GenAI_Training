from playwright.sync_api import sync_playwright


URL = "https://www.cricbuzz.com/cricket-match/live-scores"


with sync_playwright() as p:

    # Open Chromium
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    # Open Cricbuzz live scores
    page.goto(URL, wait_until="domcontentloaded")

    # Give the page a little time to load dynamic content
    page.wait_for_timeout(5000)

    print("\n========== CRICBUZZ LIVE SCORES ==========\n")

    # Get all match cards
    matches = page.locator("div.cb-mtch-lst")

    count = matches.count()

    print(f"Matches found: {count}\n")

    for i in range(count):

        match = matches.nth(i)

        try:
            # Get all visible text from this match
            text = match.inner_text().strip()

            if text:
                print("----------------------------------------")
                print(text)

        except Exception as e:
            print(f"Could not read match {i}: {e}")

    print("\n==========================================")

    # Keep browser open for a few seconds so you can see the page
    page.wait_for_timeout(5000)

    browser.close()

