import asyncio
from pyppeteer import launch

async def get_serial_number():
    browser = await launch(
        executablePath="C:/Program Files/Google/Chrome/Application/chrome.exe",
        headless=True
    )
    page = await browser.newPage()

    await page.goto("http://192.168.0.11:8087/?page=Info", waitUntil="networkidle2")

    # Check if page has an iframe
    frames = page.frames
    # print(f"Found {len(frames)} frames")

    # Find the correct iframe containing the serial number field
    for frame in frames:
        serial_number = await frame.evaluate('''() => {
            let el = document.querySelector("input[name='tbSerial']");
            return el ? el.value : null;
        }''')
        if serial_number:
            print("Camera Serial Number:", serial_number)
            break
    else:
        print("Serial number field not found in any frame.")

    await browser.close()

asyncio.run(get_serial_number())
