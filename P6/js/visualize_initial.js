// Survival Probability by Class and Sex
    var width = 700;
	var height = 400;
    var svg1 = dimple.newSvg("#chart1", width, height);
	//Read from data then generate bar chart
    d3.csv("data/survival_class.csv", function(data){
        var chart = new dimple.chart(svg1, data);
        var x = chart.addCategoryAxis("x", ["Class","Sex"]);
        var y = chart.addMeasureAxis("y", "Survival Probability");
        var s = chart.addSeries("Sex", dimple.plot.bar);
        s.addOrderRule(["Female", "All", "Male"]);
		//Create title
		svg1.append("text")
         .attr("x", chart._xPixels() + chart._widthPixels() / 2)
         .attr("y", chart._yPixels() - 20)
		 .style("font-weight", "bold")
         .style("text-anchor", "middle")
         .text("Survival Probability by Class and Sex");
    	chart.addLegend(100, 50, 510, 20, "right");
    
    	//Colors
	    chart.defaultColors = [
	    new dimple.color("#131FC8"),
	    new dimple.color("#1F79B3"),
	    new dimple.color("#80D6EE"),
		]; 
			
		chart.draw();
    });
    
// Survival Probability by Age Group
    var width = 700;
	var height = 400;
    var svg2 = dimple.newSvg("#chart2", width, height);
	//Read from data then generate bar chart
    d3.csv("data/survival_age.csv", function(data){
        var chart = new dimple.chart(svg2, data);
        var x = chart.addCategoryAxis("x", "Age");
        x.addOrderRule(["Under 15", "15-25", "25-35", "35-45", "45-55", "Above 55"]);
        var y = chart.addMeasureAxis("y", "Survival Probability");
        var s = chart.addSeries("Age", dimple.plot.bar);
        s.addOrderRule("Age",false);
		//Create title
		svg2.append("text")
         .attr("x", chart._xPixels() + chart._widthPixels() / 2)
         .attr("y", chart._yPixels() - 20)
		 .style("font-weight", "bold")
         .style("text-anchor", "middle")
         .text("Survival Probability by Age Group");    
    	 
		 //Colors
	    chart.defaultColors = [new dimple.color("#4d94ff")]; 
			
    chart.draw();
    });
