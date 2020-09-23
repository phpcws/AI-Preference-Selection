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
	document.querySelector(".topic-frameli").innerHTML = "第 " + "<div>" + select1 + "</div>" + "/" + 18 + " 题"
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
					document.querySelector(".topic-frameli").innerHTML = "第 " + "<div>" + select1 + "</div>" + "/" + 18 + " 题"
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
					document.querySelector(".topic-frameli").innerHTML = "第 " + "<div>" + select1 + "</div>" + "/" + 18 + " 题"
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
					document.querySelector(".topic-frameli").innerHTML = "第 " + "<div>" + select1 + "</div>" + "/" + 18 + " 题"
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
					document.querySelector(".topic-frameli").innerHTML = "第 " + "<div>" + select1 + "</div>" + "/" + 18 + " 题"
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
             "title": "1.（计算能力） 在面对一些繁琐的计算时（如圆锥曲线、积分运算），正确率和解题速度处于什么水平？",
            
             "xuanxiang":[
             				"正确率高且解题速度快",
             				"正确率不高但解题速度快",
             				"正确率高但解题速度不快",
             				"正确率不高且解题速度不快",
             				]
	
        },{  
             "id" : "2",  
             "title": "2.（科学能力）是否经常观看科教类的纪录片或节目？是否阅读过科普类的书籍？",
            
             "xuanxiang":[
             				"经常",
             				"偶尔",
             				"基本不",
             				"从不",
             				]
        },{  
             "id" : "3",  
             "title": "3、（抽象推理能力）如果学校出现食堂菜价过高的问题，现在你需要编写一份提案进行反映和解决，你第一时间会想到收集以下哪个数据，来最大程度地增加提案的说服力呢？",
            
             "xuanxiang":[
             				"罗列食堂菜价的前后变化",
             				"其他学校与本校的对比",
             				"学生对于食堂问题的态度反映",
             				"感觉以上答案没有区别",
             				]
        },{  
             "id" : "4",  
             "title": "4、（机械推理能力）是否了解过一些机械的工作原理和内部结构？是否拆解拼装过家中的一些小物件？",
             
             "xuanxiang":[
             				"了解过且拆解拼装过",
             				"没了解过但拆解拼装过",
             				"了解过但没拆解拼装过",
             				"没了解过且没拆解拼装过",
             				]
        },{  
             "id" : "5",  
             "title": "5.（操作能力）感觉自己的动手能力怎么样？（如按照一些说明书进行物件的组装和拆解等）",
            
             "xuanxiang":[
             				"动手能力强",
             				"动手能力较强",
             				"动手能力一般",
             				"动手能力差",
             				]
        },{  
             "id" : "6",  
             "title": "6、（助人能力）是否愿意且能够在他人遇到困难时给予有效且及时的帮助？",
             
             "xuanxiang":[
             				"愿意且能够",
             				"不愿意但是有能力做到",
             				"愿意但是常常心有余而力不足",
             				"不愿意且会帮倒忙",
             				]
        },
		{  
             "id" : "7",  
             "title": "7、（空间关系）感觉自己的空间想象能力如何？",
             
             "xuanxiang":[
             				"非常好",
             				"比较好",
             				"一般般",
             				"不太行",
             				]
        },{  
             "id" : "8",  
             "title": "8、（艺术创作能力）是否有过艺术创作经历？",
             
             "xuanxiang":[
             				"有，且获得过重要奖项",
             				"有，但没有参与过比赛",
             				"没有，但是很乐意尝试",
             				"没有且不感兴趣",
             				]
        },{  
             "id" : "9",  
             "title": "9、（音乐能力）如何评价自己的音乐能力？",
             
             "xuanxiang":[
             				"有通过一些音乐方面的等级考试或者参加过专业的声乐训练",
             				"自学过一些乐器，停留在业余兴趣的水平",
             				"有兴趣但是没有尝试过",
             				"完全不感兴趣",
             				]
        },
		{  
             "id" : "10",  
             "title": "10、（语文运用能力）平时日常交流或写作时会自然想到并恰当使用到一些成语或诗词吗？",
             
             "xuanxiang":[
             				"经常",
             				"偶尔",
							"基本不",
							"从不",
             				]
        },
		{  
             "id" : "11",  
             "title": "（亲和力）日常生活中会主动和陌生人交谈吗？在面对一些陌生人搭话时是否会感到焦虑？（如坐出租车时）",
             
             "xuanxiang":[
             				"会，且完全不焦虑",
             				"不会，但不会焦虑",
             				"会，但会感到焦虑",
             				"不会，且感到焦虑",
             				]
        },{  
             "id" : "12",  
             "title": "12、（文书速度与准确度）某学校计算机学院使用“计日迎君踏秋来”作为迎接新生的宣传用语，你觉得合适吗？",
             
             "xuanxiang":[
             				"合适，非常顺口",
             				"不能判断",
                             "不合适，但不知道具体原因",
                             "不合适，且明确原因",
             				]
        },
		{  
             "id" : "13",  
             "title": "13、（文艺创作能力）是否有过文学创作经历？",
             
             "xuanxiang":[
             				"有，且获得过重要奖项或成功投稿",
             				"有，但没有参与过比赛",
             				"没有，但是很乐意尝试",
             				"没有且不感兴趣",
             				]
        },{  
             "id" : "14",  
             "title": "14、（组织能力）是否组织过一些班级、学校活动？反响如何？",
             
             "xuanxiang":[
             				"组织过，反响好",
             				"组织过，但反响一般",
             				"没组织过，但希望尝试",
             				"没组织过，且完全没兴趣",
             				]
        },{  
             "id" : "15",  
             "title": "15、（领导能力）是否担任过班干部的职务？在同学中的号召力如何？",
             
             "xuanxiang":[
             				"担任过，号召力很强",
             				"担任过，但号召力一般",
             				"没有，但是很乐意尝试",
             				"没担任过且完全不想",
             				]
        },{  
             "id" : "16",  
             "title": "16、（销售能力）是否尝试过退销售卖物品？结果如何？",
             
             "xuanxiang":[
             				"尝试过，卖出去很多",
             				"尝试过，卖出去不多",
             				"没尝试过，但很有兴趣",
             				"没尝试过，也不想尝试",
             				]
        },{  
             "id" : "17",  
             "title": "17、(沟通能力）跟父母有分歧的时候你会如何做？",
             
             "xuanxiang":[
             				"积极跟父母沟通，寻找解决办法",
             				"能表达自己的想法，但无法说服父母",
             				"不愿表达自己的想法，沉默地听从父母的安排",
             				"跟父母争吵，强迫父母按照你的想法走",
             				]
        },{  
             "id" : "18",  
             "title": "18、（考察阅读能力）每分钟阅读中文的速度如何？",
             
             "xuanxiang":[
             				"700字以上",
             				"500-700字",
             				"350-500字",
             				"350字以下",
             				]
        },
        ];
        

