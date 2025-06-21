function solution(hp) {
    let reminder = hp % 5;
    let general = (hp - reminder) / 5;
    let worker = reminder % 3;
    let soldier = (reminder - worker) / 3;
    return general + soldier + worker;
}

console.log(solution(23));
console.log(solution(24));
console.log(solution(999));