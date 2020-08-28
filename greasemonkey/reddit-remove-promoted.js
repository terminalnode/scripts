// ==UserScript==
// @description Remove promoted links and ads on reddit.
// @include     https://www.reddit.com/*
// @version     1.0
// ==/UserScript==

console.log("UserScript Reddit Remove Promoted: Started");

// Find all elements with a matching class and delete them
function removeElementsByClassName(className) {
  let collection = document.getElementsByClassName(className);
  let removed = 0;

  while (collection.length > 0) {
    console.log(`Removing element from ${className}, number ${++removed}`)
    let element = collection.item(0);
    element.parentNode.removeChild(element)
  }
}

// Find all elements with a matching class,
// find their parents, remove their parents.
// The child can't live without it's parent.
function removeElementsParentsByClassName(className) {
  let collection = document.getElementsByClassName(className);
  let removed = 0;

  while (collection.length > 0) {
    console.log(`Removing element from ${className}, number ${++removed}`)
    let element = collection.item(0);
    element.parentNode.parentNode.removeChild(element.parentNode)
  }
}

removeElementsByClassName("promotedlink")
removeElementsParentsByClassName("premium-banner-outer")
removeElementsParentsByClassName("ad-container")

console.log("UserScript Reddit Remove Promoted: Finished")
