var snapList = document.getElementById('snap_list');
var snapItems = snapList.getElementsByClassName('snap-item');
var snapProgressBar = document.getElementById('snap_progress_bar');


function snapMagicTransition(oldItem, newItem, newIndex) {
  oldItem.style.opacity = '0';
  newItem.style.opacity = '1';

  var progressValue = 100*newIndex/(snapItems.length-1);
  if (progressValue < 1.618) {
    progressValue = 1.618;
  }
  snapProgressBar.children[0].setAttribute('aria-valuenow', progressValue);
  snapProgressBar.children[0].style.width = String(progressValue) + '%';

}

function scrollNextSnapList() {
  var index = parseInt(snapList.dataset.current);
  var oldItem;
  var newItem;
  var newIndex = index+1;

  oldItem = snapItems.item(index);
  if (snapItems.length > newIndex) {
    newItem = snapItems.item(newIndex);
    snapList.dataset.current = newIndex;

  } else {
    newItem = oldItem;
    newIndex = index;
  }

  snapMagicTransition(oldItem, newItem, newIndex);

}

function scrollPreviousSnapList() {
  var index = parseInt(snapList.dataset.current);
  var oldItem;
  var newItem;
  var newIndex = index-1;

  oldItem = snapItems.item(index);
  if (newIndex >= 0) {
    newItem = snapItems.item(newIndex);
    snapList.dataset.current = newIndex;

  } else {
    newItem = oldItem;
    newIndex = index;
  }

  snapMagicTransition(oldItem, newItem, newIndex);

}
