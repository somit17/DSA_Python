public class Solution {
    public IList<IList<int>> Generate(int numRows) {
       IList<IList<int>> result = new List<IList<int>>(); 
       if(numRows<1) return result;
       //Add 1 at start
       List<int> current = new List<int>();
       current.Add(1);
       result.Add(current);
       //2 - > numRows
       for(int i=2 ; i<=numRows;i++){
         int prev = 0;
         List<int> tempList = new List<int>();
         foreach(var num in current){
            int newVal = prev+num;
            tempList.Add(newVal);
            prev=num;
         }
         tempList.Add(1);//Add 1 at last
         result.Add(tempList);
         current=tempList;
       }
       return result;
    }
}