function solution(files) {
    const headArr = []
    const numberArr = []
    // 정규식을 이용한 HEAD, NUMBER 추출
    for (file_name of files) {
        headArr.push(file_name.match(/^\D+/)[0].toLowerCase())
        numberArr.push(parseInt(file_name.match(/\d+/)[0]))
    }
    
    // stable sort를 위한 버블소트
    for (let i = 0; i < files.length; i++) {
        let swap;
        for (let j = 0; j < files.length - i - 1; j++) {
            if (headArr[j] > headArr[j+1] || headArr[j] == headArr[j+1] && numberArr[j] > numberArr[j+1]) {
                swap = files[j];
                files[j] = files[j+1];
                files[j+1] = swap
                swap = headArr[j]
                headArr[j] = headArr[j+1];
                headArr[j+1] = swap
                swap = numberArr[j]
                numberArr[j] = numberArr[j+1];
                numberArr[j+1] = swap
            }
        }
    }
    return files;
}