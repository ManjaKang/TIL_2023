function solution(m, musicinfos) {
  musicinfos = musicinfos.map(e => {
    const arr = e.split(',')
    const duration = (new Date(`1970-01-01 ${arr[1]}:00`) - new Date(`1970-01-01 ${arr[0]}:00`)) / 60000;
    let ratioMusic = arr[3].replace(/[A-Z]#/g, n=>n[0].toLowerCase())
    ratioMusic = ratioMusic.repeat(Math.ceil(duration / ratioMusic.length)).substr(0, duration)
    return `${ratioMusic},${arr[2]},${duration}`
  })
  musicinfos.sort((a, b) => {
    a = parseInt(a.split(',')[2])
    b = parseInt(b.split(',')[2])
    return b - a
  })
  const answer = musicinfos.filter(e => 
    e.split(',')[0].indexOf(m.replace(/[A-Z]#/g,n=>n[0].toLowerCase())) !== -1
  ) 
  return answer.length === 0 ? '(None)' : answer[0].split(',')[1];
}
