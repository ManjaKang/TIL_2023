function solution(n, t, m, timetable) {
  var answer = '';
  const minArr = []
  for (time of timetable) {
    minArr.push(timeToMin(time))
  }
  minArr.sort()
  let busTime = 540
  while (minArr) {
    let crewTime = minArr.shift()
    if (busTime < crewTime) {
      busTime += t
    }
  }
  return minArr;
}

function timeToMin(time) {
  const times = time.split(':')
  return parseInt(times[0]) * 60 + parseInt(times[1])
}