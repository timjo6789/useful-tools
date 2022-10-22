// credit: https://stackoverflow.com/a/46118025
function copyToClipboard(text) {
    var dummy = document.createElement("textarea");
    document.body.appendChild(dummy);
    dummy.value = text;
    dummy.select();
    document.execCommand("copy");
    document.body.removeChild(dummy);
}


let output = '';
for(let item of document.querySelectorAll('div.module-item-title a')) {
    output += item.text.replaceAll('\n', '').trim()+ ' -> ' + item.href.trim() + '\n';
}
copyToClipboard(output);
