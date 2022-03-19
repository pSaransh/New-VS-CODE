/**
!! Python -> in
!! 's' in 'sherlock' -> returns True
!! 'y' in 'star wars' -> return False
!! String s = "sherlock";
!! s.in("s"); -> True
* this function is case senstive
* this class is available for everyone out there so implement your own functions devs
* @author Ramansh Pathak
* @see https://stackoverflow.com/questions/9418729/extend-java-lang-string#:~:text=You%20cannot%20extend%20a%20class,goes%20into%20creating%20String%20classes.
* Thanks to JON SKEET
*/
public class StringPython {
    private final String theRealString;
    private final Exception inWithNull = new Exception("\nPlease don't make me curse you. <3\nPlease don't use null values to compare.");
    public StringPython(String theRealString) {
        this.theRealString = theRealString;
    }        
    public boolean in(String toCompareWith) throws Exception{
        if(toCompareWith==null)
                throw inWithNull;   
        return theRealString.indexOf(toCompareWith) == -1 ? false : true ;
    }
    
}
