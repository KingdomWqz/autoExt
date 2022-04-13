import {
  querySelectorAllDeep,
  querySelectorDeep,
} from "query-selector-shadow-dom";
const ins = querySelectorAllDeep("#option");
// console.log(ins);

/** ====== Simulate Human Click ======= */

let btn = null;

const onDown = (e) => {
  chrome.runtime.sendMessage(
    {
      event: "mousedown",
      x: 0,
      y: 0,
    },
    (response) => {
      console.log(response);
    }
  );
};

setTimeout(() => {
  console.log("RPA Simulate Human Click: starting");
  btn = document.querySelector(".logo-link");

  // window.addEventListener("keydown", onDown, true);
  // window.addEventListener("mousedown", onListener, true);
  // window.addEventListener("click", onDown, true);
}, 300);
