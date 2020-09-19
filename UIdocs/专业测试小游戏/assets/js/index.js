function TiMu(){
	for(var i in data1){
		var div = document.createElement("div");
		div.className = "entrance-bottom-frame-line";
		document.querySelector(".entrance-bottom-frame").appendChild(div);
		
		
		var div2 = document.createElement("div");
		div2.className = "entrance-bottom-frame-line-title";
		div2.innerHTML = data1[i].title;
		document.querySelectorAll(".entrance-bottom-frame-line")[i].appendChild(div2);
			
		
		var divli1 = document.createElement("div");
		divli1.innerHTML = parseInt(i) + 1;
		
		var timu = 1
		for(var j in data1[i].xuanxiang){
			var div3 = document.createElement("div");
			div3.className = "entrance-bottom-frame-line-button";
			var div3_id = document.createElement("div");
			div3_id.className = "entrance-bottom-frame-line-button-id";
			if(j == 0){
				 div3_id.innerHTML = "A";
			}else if(j == 1){
				 div3_id.innerHTML = "B";
			}else if(j == 2){
				 div3_id.innerHTML = "C";
			}else{
				 div3_id.innerHTML = "D";
			}
			var div4 = document.createElement("div");
			div4.className = "entrance-bottom-frame-line-button-frame";
			div4.innerHTML = data1[i].xuanxiang[j];
			div3.appendChild(div3_id)
			div3.appendChild(div4);
			document.querySelectorAll(".entrance-bottom-frame-line")[i].appendChild(div3);
			timu++
		}
	}
	mintime = 1; 
	var dact = document.querySelector(".entrance-bottom-frame-line")
	var active = "active"
	var none = "none"
	addClass(dact, active)
	var timu_id = 0
	var select1 = 1
	var frame_left = 0
	var A=0
	var B=0
	var C=0
	var D=0
	document.querySelector(".entrance-bottom-frame").style.marginLeft = frame_left + "%"
	document.querySelector(".topic-frameli").innerHTML = "第 " + "<div>" + select1 + "</div>" + "/" + timu + " 题"
	for(var i = 0;i<document.querySelectorAll(".entrance-bottom-frame-line-button").length;i++){
		if(i%4==0) {
			document.querySelectorAll(".entrance-bottom-frame-line-button")[i].onclick = function () {
				if (timu_id < document.querySelectorAll(".entrance-bottom-frame-line").length - 1) {
					/*alert("A")*/
					frame_left += -100
					document.querySelector(".entrance-bottom-frame").style.marginLeft = frame_left + "%"
					timu_id++;
					select1++;
					A++;
					document.querySelector(".topic-frameli").innerHTML = "第 " + "<div>" + select1 + "</div>" + "/" + timu + " 题"
					addClass(document.querySelectorAll(".entrance-bottom-frame-line")[timu_id], active)
					removeClass(document.querySelectorAll(".entrance-bottom-frame-line")[timu_id - 1], active)

				} else {
					A++
					var result="你选择A"+A+"个,"+"你选择B"+B+"个,"+"你选择C"+C+"个,"+"你选择D"+D+"个。"
					alert(result)
				}
			}
		}
		if(i%4==1) {
			document.querySelectorAll(".entrance-bottom-frame-line-button")[i].onclick = function () {
				if (timu_id < document.querySelectorAll(".entrance-bottom-frame-line").length - 1) {
					frame_left += -100
					document.querySelector(".entrance-bottom-frame").style.marginLeft = frame_left + "%"
					timu_id++;
					select1++;
					B++;
					document.querySelector(".topic-frameli").innerHTML = "第 " + "<div>" + select1 + "</div>" + "/" + timu + " 题"
					addClass(document.querySelectorAll(".entrance-bottom-frame-line")[timu_id], active)
					removeClass(document.querySelectorAll(".entrance-bottom-frame-line")[timu_id - 1], active)

				} else {
					B++
					var result="你选择A"+A+"个,"+"你选择B"+B+"个,"+"你选择C"+C+"个,"+"你选择D"+D+"个。"
					alert(result)
				}
			}
		}
		if(i%4==2) {
			document.querySelectorAll(".entrance-bottom-frame-line-button")[i].onclick = function () {
				if (timu_id < document.querySelectorAll(".entrance-bottom-frame-line").length - 1) {
					frame_left += -100
					document.querySelector(".entrance-bottom-frame").style.marginLeft = frame_left + "%"
					timu_id++;
					select1++;
					C++;
					document.querySelector(".topic-frameli").innerHTML = "第 " + "<div>" + select1 + "</div>" + "/" + timu + " 题"
					addClass(document.querySelectorAll(".entrance-bottom-frame-line")[timu_id], active)
					removeClass(document.querySelectorAll(".entrance-bottom-frame-line")[timu_id - 1], active)

				} else {
					C++
					var result="你选择A"+A+"个,"+"你选择B"+B+"个,"+"你选择C"+C+"个,"+"你选择D"+D+"个。"
					alert(result)
				}
			}
		}
		if(i%4==3) {
			document.querySelectorAll(".entrance-bottom-frame-line-button")[i].onclick = function () {
				if (timu_id < document.querySelectorAll(".entrance-bottom-frame-line").length - 1) {
					frame_left += -100
					document.querySelector(".entrance-bottom-frame").style.marginLeft = frame_left + "%"
					timu_id++;
					select1++;
					D++;
					document.querySelector(".topic-frameli").innerHTML = "第 " + "<div>" + select1 + "</div>" + "/" + timu + " 题"
					addClass(document.querySelectorAll(".entrance-bottom-frame-line")[timu_id], active)
					removeClass(document.querySelectorAll(".entrance-bottom-frame-line")[timu_id - 1], active)

				} else {
					D++
					var result="你选择A"+A+"个,"+"你选择B"+B+"个,"+"你选择C"+C+"个,"+"你选择D"+D+"个。"
					alert(result)
				}
			}
		}
	}

}

function addClass(obj, cls){
  var obj_class = obj.className,//获取 class 内容.
  blank = (obj_class != '') ? ' ' : '';//判断获取到的 class 是否为空, 如果不为空在前面加个'空格'.
  added = obj_class + blank + cls;//组合原来的 class 和需要添加的 class.
  obj.className = added;//替换原来的 class.
}

function removeClass(obj, cls){
  var obj_class = ' '+obj.className+' ';//获取 class 内容, 并在首尾各加一个空格. ex) 'abc    bcd' -> ' abc    bcd '
  obj_class = obj_class.replace(/(\s+)/gi, ' '),//将多余的空字符替换成一个空格. ex) ' abc    bcd ' -> ' abc bcd '
  removed = obj_class.replace(' '+cls+' ', ' ');//在原来的 class 替换掉首尾加了空格的 class. ex) ' abc bcd ' -> 'bcd '
  removed = removed.replace(/(^\s+)|(\s+$)/g, '');//去掉首尾空格. ex) 'bcd ' -> 'bcd'
  obj.className = removed;//替换原来的 class.
}

function hasClass(obj, cls){
  var obj_class = obj.className,//获取 class 内容.
  obj_class_lst = obj_class.split(/\s+/);//通过split空字符将cls转换成数组.
  x = 0;
  for(x in obj_class_lst) {
    if(obj_class_lst[x] == cls) {//循环数组, 判断是否包含cls
      return true;
    }
  }
  return false;
}



var data1 =[ {
             "id" : "1",  
             "title": "1. 你觉得孔祥龙帅吗？",
            
             "xuanxiang":[
             				"帅",
             				"谁说不帅",
             				"必须帅",
             				"YES",
             				]
	
        },{  
             "id" : "2",  
             "title": "你觉得孔祥龙帅吗？",
            
             "xuanxiang":[
             				"帅",
             				"谁说不帅",
             				"必须帅",
             				"YES",
             				]
        },{  
             "id" : "3",  
             "title": "你觉得孔祥龙帅吗？",
            
             "xuanxiang":[
             				"帅",
             				"谁说不帅",
             				"必须帅",
             				"YES",
             				]
        },{  
             "id" : "4",  
             "title": "你觉得孔祥龙帅吗？",
            
             "xuanxiang":[
             				"帅",
             				"谁说不帅",
             				"必须帅",
             				"YES",
             				]
        },{  
             "id" : "5",  
             "title": "你觉得孔祥龙帅吗？",
             
             "xuanxiang":[
             				"帅",
             				"谁说不帅",
             				"必须帅",
             				"YES",
             				]
        }
        ];
        

