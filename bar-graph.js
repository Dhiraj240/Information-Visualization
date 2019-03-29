d3.json('jsondata.json', function(data){
	d3.select('body')
	.selectAll('p')
	.data(data)
	.enter()
	.append('p')
	.text(function(d){
		return d.id + '\'individual name is' + d.Name + '.A profession description' + d.description + 'with category indicating M as Male and F as Female' + d.category;
	});
});