var snapList = document.getElementById('snap_list');
var snapItems = snapList.getElementsByClassName('snap-item');


function snapMagicTransition(oldItem, newItem) {
  oldItem.style.opacity = '0';
  newItem.style.opacity = '1';

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
  }

  snapMagicTransition(oldItem, newItem);

}

function scrollPreviousSnapList() {
  var index = parseInt(snapList.dataset.current);
  var oldItem;
  var newItem;
  var newIndex = index-1;

  oldItem = snapItems.item(index);
  if (snapItems.length > newIndex) {
    newItem = snapItems.item(newIndex);
    snapList.dataset.current = newIndex;

  } else {
    newItem = oldItem;
  }

  snapMagicTransition(oldItem, newItem);

}
