// One trick to organizing code is to put related functions inside of an object,
// so they are under the same "namespace". This helps make readable code that is
// easier to maintain in the long term.

// TODO: replace use of `document.getElementByXXX` with `d3.select` so it is more readable

/* globals scrollama */

const Project = {};

Project.scrolling = {
  // these hold references to helpers and rendered page elements (filled in by `initialize`)
  scroller: undefined, // an instance of scrollama
  steps: undefined, // an array of all the step elements

  // a list of the backdrop images, ordered so they match the `step` elements on the page
  backdrops: [
    {
      src: "https://barrfdn-prod.s3.amazonaws.com/crop/566/halfscreen_crop.jpg?1529008399",
      credit:"https://www.barrfoundation.org/partners/raising-a-reader-massachusetts",
      type: "image",
    },
    //CHECK COPYWRITE
    {
      src: "https://darwinproject.org/wp-content/uploads/2020/01/rar-photo-4.jpg",
      credit:"https://darwinproject.org/projects/raising-a-reader-massachusetts/",
      type: "image",
    },
    //CHECK COPYWRITE
    {
      src: "https://darwinproject.org/wp-content/uploads/2020/01/rar-photo-2.jpg",
      credit:"https://darwinproject.org/projects/raising-a-reader-massachusetts/",
      type: "image",
    },
    //CHECK COPYWRITE
    
    {
      src: "https://cdn.glitch.global/05db6cb4-1854-4ed6-a375-b75526b503d1/2024.9.18_MerrimackValleyYMCA_GustavoCruz%26EllieRose_Photo3.jpg?v=1738267781832",
      credit:"https://raisingareaderma.org/",
      type: "image",
    },
    {
      src: "https://cdn.glitch.global/05db6cb4-1854-4ed6-a375-b75526b503d1/2024.11.13_BarrettRussellFEIBrockton_FabwaRodriguesAdonis_Photo1.jpg?v=1738267767016",
      credit:"https://raisingareaderma.org/",
      type: "image",
    },
    {
      src: "https://cdn.glitch.global/05db6cb4-1854-4ed6-a375-b75526b503d1/Leo%20Mckinney%20Pecora%20picture.jpg?v=1738267817693",
      credit:"https://raisingareaderma.org/",
      type: "image",
    },
  ],

  
  // set up the webpage to scroll
  initialize: () => {
    // grab the elements on the page that are related to the scrolling
    const scrollWrapper = document.getElementById("scrolly");
    Project.scrolling.figure = scrollWrapper.getElementsByTagName("figure")[0];

    const article = scrollWrapper.getElementsByTagName("article")[0];
    Project.scrolling.steps = Array.from(
      article.getElementsByClassName("step")
    );
    
    // convert from HTMLCollection to Array for ease of use later
    // intialize the scrollama helper
    Project.scrolling.scroller = scrollama();
    Project.scrolling.scroller
      .setup({
        step: "#scrolly article .step",
        offset: 0,
        debug: false,
      })
      .onStepEnter(Project.scrolling.handleStepEnter)
      .onStepExit(Project.scrolling.handleStepExit);
    
    // setup the default view to be the right size and include first step
    Project.scrolling.handleResize();
    Project.scrolling.setBackdropImage(0); // remember: 0 means the first item in an array
  },

  
  // call this to switch the background image
  setBackdropImage: (index) => {
    // grab the info for this step
    // if this step's type is image
    //   then swap the image
    // if this step's type is video
    //   hide the image
    //   set the video src
    //   show the video
    //   play the video
    const image = Project.scrolling.figure.getElementsByTagName("img")[0];
    image.src = Project.scrolling.backdrops[index].src;
    //image.classList.add = 'fade-in';
    // TODO: make this caption text a link
    document.getElementsByTagName("figcaption")[0].innerHTML =
      Project.scrolling.backdrops[index].credit;
  },

  // called by scrollama when the step is being entered
  handleStepEnter: (stepInfo) => {
    // stepInfo = { element, directihandle, index }
    // console.log(`Switched to step ${stepInfo.index}`);

    
    // ATTEMPTED BUT IT FUCKED EVERYTHING UP:
    // TO DO: 
    // Remove active class from all steps
    // Project.scrolling.steps.forEach(step => step.classList.remove('is-active'));
    // Add active class to the current step
    //stepInfo.element.classList.add('is-active');
    
    Project.scrolling.setBackdropImage(stepInfo.index);
  },

  // called by scrollama when moving out of a step
  handleStepExit: (stepInfo) => {
    // we don't make any transitions when a step scrolls out of view
  },

  // called to get content to be the right size to fit the device
  handleResize: () => {
    const stepH = Math.floor(window.innerHeight * 1); // update step heights
    Project.scrolling.steps.forEach(
      (step) => (step.style.height = stepH + "px")
    );
    const figureWidth = window.innerWidth;
    const figureHeight = window.innerHeight;
    Project.scrolling.figure.style.width = figureWidth + "px";
    Project.scrolling.figure.style.height = figureHeight + "px";
    Project.scrolling.figure.style.top = "0px";
    Project.scrolling.figure.getElementsByClassName("wrapper")[0].style.height =
      figureHeight + "px";
    Project.scrolling.scroller.resize(); // tell scrollama to update new element dimensions
  },
};



/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}