
console.log('panel');
document.querySelector('#btnEl').addEventListener('click', getElement);

document.querySelector('#btnInspect').addEventListener('click', startInspect);

function startInspect() {
    chrome.devtools.inspectedWindow.eval('inspect(document.body)');
}

function getElement() {
    chrome.devtools.inspectedWindow.eval("setSelectedElement($0)",
    { useContentScriptContext: true });
}