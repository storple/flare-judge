var clipboard = new ClipboardJS(
    '.code-clipboard',
    {
        target: function(trigger) {
            return trigger.nextSibling;
        }
    }
);

clipboard.on('success', function(e) {
    e.clearSelection();
});
