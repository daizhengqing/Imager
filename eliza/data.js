// import axios from 'axios'

// const auth_token = "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"

// const $http = axios.create({
//   headers: {
//     'Authorization': auth_token,
//     'Cache-control': 'no-cache',
//     'Content-Type': 'application/json',
//     'X-twitter-active-user': 'yes',
//     'X-twitter-auth-type': 'OAuth2Session',
//     'X-twitter-client-language': 'zh-cn'
//   }
// })

// let cursor = null

// const variables = {
//   rawQuery: "$eliza",
//   count: 50,
//   querySource: "typed_query",
//   product: "Top",
//   cursor
// };

// const features = {
//   rweb_tipjar_consumption_enabled: true,
//   responsive_web_graphql_exclude_directive_enabled: true,
//   verified_phone_label_enabled: false,
//   creator_subscriptions_tweet_preview_api_enabled: true,
//   responsive_web_graphql_timeline_navigation_enabled: true,
//   responsive_web_graphql_skip_user_profile_image_extensions_enabled: false,
//   communities_web_enable_tweet_community_results_fetch: true,
//   c9s_tweet_anatomy_moderator_badge_enabled: true,
//   articles_preview_enabled: true,
//   responsive_web_edit_tweet_api_enabled: true,
//   graphql_is_translatable_rweb_tweet_is_translatable_enabled: true,
//   view_counts_everywhere_api_enabled: true,
//   longform_notetweets_consumption_enabled: true,
//   responsive_web_twitter_article_tweet_consumption_enabled: true,
//   tweet_awards_web_tipping_enabled: false,
//   creator_subscriptions_quote_tweet_preview_enabled: false,
//   freedom_of_speech_not_reach_fetch_enabled: true,
//   standardized_nudges_misinfo: true,
//   tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled: true,
//   rweb_video_timestamps_enabled: true,
//   longform_notetweets_rich_text_read_enabled: true,
//   longform_notetweets_inline_media_enabled: true,
//   responsive_web_enhance_cards_enabled: false,
// };

// async function login () {

// }

// const search  = async () => {
//   const data  = await $http.get('https://x.com/i/api/graphql/MJpyQGqgklrVl_0X9gNy3A/SearchTimeline', {
//     params: {
//       variables,
//       features
//     }
//   })
// }
import puppeteer from "puppeteer";

async function loginX() {
  const browser = await puppeteer.launch({
    headless: false
  })

  const page = await browser.newPage()
  page.setDefaultNavigationTimeout(50000)
  await page.setUserAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36')
  await page.goto('https://x.com/i/flow/login')
  await page.screenshot({
    path: 'loginf.png'
  })
  
  await page.waitForSelector('input')
  await page.type('input', 'ddzq789@outlook.com')
  await page.evaluate(() => {
    document.querySelector('input').parentElement.parentElement.parentElement.parentElement.parentElement.nextElementSibling.click()
  })

  await page.waitForSelector('input')

  if (await page.content('手机号码')) {
    await page.type('input', 'likelikerena')
    await page.evaluate(() => {
      document.querySelector('input').parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.nextElementSibling.querySelector('button').click()
    })
  }

  await page.waitForSelector('input[autocomplete="current-password"]')
  await page.type('input[autocomplete="current-password', 'ddzq2957578')
  await page.evaluate(() => {
    document.querySelector('input[autocomplete="current-password"]').parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.nextElementSibling.querySelector('button').click()
  })

  await page.waitForNavigation()
  await page.goto('https://x.com/explore')
  await page.waitForSelector('input')
  await page.type('input', 'x.com')
  await page.keyboard.press('Enter')
  await page.setRequestInterception(true)
  page.on('request', async req => {
    if (req.url().includes('SearchTimeline')) {
      take({
        url: req.url(),
        params: req.postData(),
        method: req.method(),
        head: req.headers(),
      })

      await browser.close()
    }

    req.continue()
  })
}

function take (baseReq) {
  console.log('base', baseReq)
}

await loginX()

