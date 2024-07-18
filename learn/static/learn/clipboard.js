var clipboard = new ClipboardJS(
    '.code-clipboard',
    {
        target: function(trigger) {
            return trigger.nextSibling;
        }
    }
);

clipboard.on('success', function(e) {
    e.trigger.dispatchEvent(new CustomEvent('clipboard_notfication', { bubbles: true }));
    e.clearSelection();
});
