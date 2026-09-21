import React, { useState } from 'react'

const App = () => {

  const [url,setUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");
  const [loading , setLoading] = useState(false);
  const [error, setError] = useState("");

  function isValidUrl(value){
    try {
      new URL(value);
      return true;
    } catch  {
      return false;
    }
  }

  async function shortenUrl(){

    setError("")
    setShortUrl("")

    if(!url.trim()){
      setError("Please Enter a URL");
      return;
    }

    if(!isValidUrl(url)){
      setError("Please enter a Valid URL");
      return
    }

    setLoading(true);

    try{
      const response = await fetch(
        "http://127.0.0.1:8000/urls",
        {
          method: "POST",

          headers: {
            "Content-Type" : "application/json"
          },

          body: JSON.stringify({
            long_url: url
          })
        }
      );

      if(!response.ok){
        throw new error("Failed to shorten URL");
      }
      const data = await response.json();

      setShortUrl(data.short_url);
  }
  catch(error){
    setError(error.message);
  }
  finally{
    setLoading(false);
  }

}

  function copyUrl(){
    navigator.clipboard.writeText(shortUrl)
  };

  return (
    <div>
      <h1>URL Shortener</h1>

      <input
      type="text"
      placeholder='Enter your long URL'
      value={url} 
      onChange={(e) => setUrl(e.target.value)}
      />

      <button
      onClick={shortenUrl}
      disabled={loading}>
        {loading ? "Shortening..." : "Shorten URL"}
        {error && (
          <p>
            {error}
          </p>
        )}
      </button>

      {shortUrl && (
        <div>
          <p>
            Short URL : {shortUrl}
          </p> 

          <button onClick={copyUrl}>
            
            Copy
          </button>

          
        </div>
         
      )}
    </div>
  )
}

export default App