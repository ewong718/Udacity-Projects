# Data Visualization: Titanic Data Visualization
#### Edmund Wong


### Summary

The Titanic was one of the most infamous shipwrecks in history and much could be learned from this disaster. 
We can visualize from these bar charts the likelihood of survival based on certain groups of passengers.
These groups are identified by the passenger age, boarding class, and sex.


### Design

For this titanic dataset, I decided to use variables that have shown some trend with survival, as I observed 
from an earlier project in this course. It is clear that survival probability is lower for males and lower
class. Also, children were more likely to be rescued. I decided to produce bar charts for passenger age, 
class, and sex and their relationship with survival probability. Survival probability was calculated from 
the original dataset file, and new smaller files were produced as the input data for these graphs.

I used dimple.js to implement the bar charts. Because sex and class had too few categories on their own, I decided
to merge them into a single graph. I divided age into six intervals, which I believe is sufficient to
produce its own standalone graph. The height of each bar corresponds to that particular group of passenger.

I added a legend to the first graph for viewers to identify sex. Following feedback, I tuned the legend. 
For aesthetics, I chose colors that were easy on the eyes and contrasted nicely with each other.
A short transition was added to both of these graphs, which adds some flair for the viewer. The viewer is
also able to interact with the graph by hovering the cursor over each bar, generating a bubble with
relevant information of that bar.


### Feedback

1. The first feedback stated that both graphs provided very interesting information but the color set choice wasn't optimal 
as all the colors were of similar hue. Perhaps a set of colors that contrast nicely with each other should be implemented.
Also, a webpage title needs to be added.

2. The second feedback provided similar feedback, except added that the legend items (sex) should be sorted in the same way
as the order in the graph.

3. The last feedback simply mentioned that my graphs were a bit bland. Somehow, they should be more dynamic.


### Resources

http://dimplejs.org/examples_viewer.html?id=bars_vertical_grouped

https://github.com/PMSI-AlignAlytics/dimple/wiki/dimple.axis

http://alignedleft.com/

2016