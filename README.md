The Deployer web app deploys static sites to their appropriate web roots.  
  
Use this as the last step in the freejekyllbuilder pipeline.  

Basically after freejekyllbuilder builds your site, send a request to the Deployer.  
The Deployer fetches the built site from freejekyllbuilder and unzips it into the web root.
