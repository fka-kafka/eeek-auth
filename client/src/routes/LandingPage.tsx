import React from "react";
import "../assets/styles/landingPage.css";

const LandingPage = () => {
  return (
    <main className="landingPage">
      <div className="landingPage_content">
        <section className="landingPage_introduction">
          <h1 className="landingPage_title">eeek!</h1>
          <article className="landingPage_article">
            <p className="landingPage_tagLine">
              Old TVs? obsolete equipment? — we re-purpose
              <br />
              your 'junk' from being yet <b>another</b> reason a
              turtle
              <br />
              chokes to death in its natural habbitat.
            </p>
          </article>
          <div className="landingPage_div">
            <a className="landingPage_a" href={"/signup"}>
              Get started
            </a>
          </div>
        </section>
      </div>
      <div className="landingPage_image"></div>
    </main>
  );
};

export default LandingPage;
