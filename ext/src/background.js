console.log("RPA Test: background is running");

let curTab;
const attachedTabs = {};
const version = "1.3";

chrome.browserAction.onClicked.addListener((tab) => {
  curTab = tab;
  const debuggee = { tabId: curTab.id };

  if (!attachedTabs[curTab.id]) {
    chrome.debugger.attach(debuggee, version, onAttach.bind(null, debuggee));
  } else {
    chrome.debugger.detach(debuggee, onDetach.bind(null, debuggee));
  }
});

// setTimeout(() => {
//   console.log('starting');
//   const debuggee = { extensionId: "pkgccpejnmalmdinmhkkfafefagiiiad" };

//   chrome.debugger.attach(debuggee, version, onAttach.bind(null, debuggee));
// }, 15000);

window.run = async () => {
  let x = 925; //970;
  let y = 455; //330;

  chrome.debugger.sendCommand(
    { tabId: curTab.id },
    "Input.dispatchMouseEvent",
    { type: "mousePressed", x, y, button: "left", clickCount: 1 },
    function (e) {
      console.log("mousePressed", e);
    }
  );
  x = x + 5;
  await sleep();

  for (; x < 1206; x = x + 5) {
    chrome.debugger.sendCommand(
      { tabId: curTab.id },
      "Input.dispatchMouseEvent",
      { type: "mouseMoved", x, y, button: "left", clickCount: 1 },
      function (e) {
        console.log("mouseMoved", e);
      }
    );
    await sleep();
  }

  chrome.debugger.sendCommand(
    { tabId: curTab.id },
    "Input.dispatchMouseEvent",
    { type: "mouseReleased", x, y, button: "left", clickCount: 1 },
    function (e) {
      console.log("mouseReleased", e);
    }
  );
};

const onAttach = (debuggee) => {
  if (chrome.runtime.lastError) {
    alert(chrome.runtime.lastError.message);
    return;
  }

  attachedTabs[debuggee.tabId] = "working";
  console.log("attach succeed");
};

const onDetach = (tabId) => {
  delete attachedTabs[tabId];
  console.log("detach succeed");
};

const sleep = () => {
  return new Promise((resolve) => setTimeout(resolve, 1000));
};
