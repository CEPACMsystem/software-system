var h5s = document.getElementsByTagName('h5')
var len = h5s.length
console.log(len);
for (var i = 0; i < len; i++) {
	h5s[i].onclick = function(){
		// alert(this.innerText)
		// 把所有的ilist收起来，不显示
		for(var j = 0; j < len; j++){
			if(h5s[j] != this)   //如果不是当前元素
				h5s[j].nextElementSibling.style.display = 'none'
		}
		
		var nextsibling = this.nextElementSibling
		if(nextsibling.style.display == 'block')
		    nextsibling.style.display = 'none'
		else
			nextsibling.style.display = 'block'
	}
}