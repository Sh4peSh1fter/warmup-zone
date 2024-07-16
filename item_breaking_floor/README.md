# Item Breaking Floor
## Background
you are given a box filled with identical items (they share the same properties).
you are near a tower with many floors.
you are told that the item might break in a certain range of floors, but you need to find the specific floor it starts to break on.
for future references we will call it the "breaking floor".
same item can be thrown as many times as we want until it breaks, which happens only when thrown from the breaking floor or higher, and it does not change as a result of previous throws.

## Requirements
there are few different goals to achieve, so write a function for each:
1. a function that finds the breaking floor as fast as possible (minimal attempts).
2. now we have a very small and limited amount of items. we need a function that finds the breaking floor with minimal number of broken items as possible, while still trying as fast as possible (minimal attempts but as second priority).

each function will get:
* starting floor
* ending floor
* breaking floor (optional) - this parameter should be used only to determine if the item was broken or not when thrown from a given floor.

and return:
* number of attempts
* number of broken items
* guessed breaking floor