session = 'AQEDASScVWAFvOrnAAABiJtt5fUAAAGMPlkxtk0AjtdFplUJ0AIu8vGYEnZnvWLR30Jod1RruAZZf662z73B_58sSQfPzWT5jFNs4X2aPL_SufHaSPxpcfC4ripdPMwCnoqP9IRpD66bb4Oii84wC534'

const { LinkedInProfileScraper } = require('linkedin-profile-scraper');

(async() => {
  const scraper = new LinkedInProfileScraper({
    sessionCookieValue: session,
    keepAlive: false
  });

  // Prepare the scraper
  // Loading it in memory
  await scraper.setup()

  const result = await scraper.run('https://www.linkedin.com/in/mfdlg/')
  
  console.log(result)
})()