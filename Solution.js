function solution(N) {
    if (N.length <= 1) {
        return N;
    }

    let mid = Math.floor(N.length / 2);
    let left = N.slice(0, mid);
    let right = N.slice(mid);

    let sortedLeft = solution(left);
    let sortedRight = solution(right);

    return merge(sortedLeft, sortedRight);
}

function merge(left, right) {
    let sortedList = [];
    let i = 0, j = 0;

    while (i < left.length && j < right.length) {
        if (left[i] < right[j]) {
            sortedList.push(left[i++]);
        } else {
            sortedList.push(right[j++]);
        }
    }

    while (i < left.length) {
        sortedList.push(left[i++]);
    }

    while (j < right.length) {
        sortedList.push(right[j++]);
    }

    return sortedList;
}