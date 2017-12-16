// v0.12.0 puppeteer
const puppeteer = require('puppeteer');
const fs = require('fs');
const crypto = require('crypto');

var outputDir = './data/html/';

async function headless(url, offset) {

    var sleep_time = Math.floor(Math.random() * 15) + 1;
    await delay(sleep_time * 1000);

    const browser = await puppeteer.launch({
        ignoreHTTPSErrors: true,
        // headless: false,
    });
    const page = await browser.newPage();

    page.emulate({
        viewport: {
            width: 1024,
            height: 768,
        },
        // macbook pro
        userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    });

    try {

        // timeout at 5 minutes (5 * 60 * 1000ms), network idle at 3 seconds
        await page.goto(url, {
            waitUntil: 'load',
            timeout: 300000,
        });

        // Get page content (html, xml, etc)
        const cont = await page.content();
        await fs.writeFile(outputDir + offset +".html", cont, function(err) {
            if (err) {
                return console.log(err);
            }
            console.log("The file was saved!");
        });

    } catch (e) {
        console.log("Failed with error:", e);
        process.exit(1);
    }

    browser.close();
}

function delay(time) {
   return new Promise(function(resolve) {
       setTimeout(resolve, time)
   });
}

// iterate through and save html
for(var i = 0; i < 13; i++){
    var temp = i;
    if (i != 0){
        temp = i * 10;
    }
    var url = "https://scholar.google.com/scholar?start=" + temp + "&q=%22term+dependency%22+%7C+%22term+dependencies%22+%7C+%22term+dependent%22+source:%22ACM+SIGIR%22&hl=en&as_sdt=0,47&as_ylo=2000";
    headless(url, temp).then(v => {
        // Once all the async parts finish this prints.
        console.log("Finished Headless");
        console.log(url);
    })
}
