// ==UserScript==
// @description Mark links on reddit as read when previewed.
// @include     https://www.reddit.com/*
// @version     1.1
// ==/UserScript==

// TODO Add list of image hosts and only do titleText link replacements for those.

console.log("UserScript Reddit Mark Read: Started");

function markRead(url) {
  currentUrl = window.location.href;
  history.replaceState({}, "", url);
  history.replaceState({}, "", currentUrl);
}

const siteTable = document.querySelector("#siteTable");

if (siteTable) {
  const linkItems = siteTable.children;

  for (item of linkItems) {
    // Fetch expand button and title text, continue if either doesn't exist
    let expandButton = item.querySelector(".expando-button");
    let titleText = item.querySelector(".entry > .top-matter > .title > a");
    if (!expandButton || !titleText) {
      continue;
    }

    // Get URL from titleText.
    // If URL is from another origin change the link to point to the comments.
    let url = titleText.href;
    let comments = item.querySelector(".entry > .top-matter > ul > .first > a");
    if (comments && !url.includes("https://www.reddit.com")) {
      url = comments.href;
      titleText.setAttribute("href", comments.href);
    }

    // Make it so the expand button marks URL as read on click.
    expandButton.addEventListener('click', function() {
      console.log(`Trying to add URL to history: ${url}`);
      markRead(url);
    }, false);
  }
}

console.log("UserScript Reddit Mark Read: Finished");
