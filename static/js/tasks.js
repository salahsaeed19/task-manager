document.addEventListener('DOMContentLoaded', function () {
    var taskList = document.getElementById('task-list');
    new Sortable(taskList, {
        animation: 150,
        onEnd: function (evt) {
            console.log(`Task moved from ${evt.oldIndex} to ${evt.newIndex}`);
        },
    });
});
