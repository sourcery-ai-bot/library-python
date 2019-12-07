// Selection sort algorithm

function selectionSort(array) {
  for (let i = 0; i < array.length; i++) {
    var minIndex = i;
    for (let j = i + 1; j < array.length; j++) {
      if(array[j] < array[minIndex]) {
        minIndex = j;
      }
    }
    if (minIndex != i) {
      let temp = array[i];
      array[i] = array[minIndex];
      array[minIndex] = temp;
    }
  }
  return array;
}

unsortedSquareNums = [49, 81, 1, 9, 36, 64, 81, 100, 4, 16, 25]

sortedSquareNums = selectionSort(unsortedSquareNums);
console.log(`The sorted square numbers list is ${sortedSquareNums}`);
