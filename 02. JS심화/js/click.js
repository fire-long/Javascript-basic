//1. 필요한 태그들 가져오기
let num = document.getElementById('num');
let btns = document.getElementsByTagName("button")

// 2-1. -1 감소 버튼 클릭 시 이벤트 처리
btns[0].onclick = () => {
    // 2-3. 단, 음수가 나오지 않게끔 조건 부여
    if(num.innerText>0){
        //2-2. p 태그 안쪽에 있는 숫자를 1 감소 시키기
        num.innerText = num.innerText-1;
    }
}

// 3-1. +1 증가 버튼 클릭 시 이벤트 처리
btns[1].onclick = () => {
    // 3-2. p태그 안쪽에 있는 숫자를 1 증가 시키기
    num.innerText ++; //그냥 +1하면 문자가 붙음 -> ++로 바꾸기!
}