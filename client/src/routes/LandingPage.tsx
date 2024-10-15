import React from "react";
import "../assets/styles/root.css";

const LandingPage = () => {
  return (
    <main className="landingPage">
      <div className="content">
        <section className="introduction">
          <h1 className="title">eeek!</h1>
          <article className="tagLine_article">
            <p className="tagLine">
              Old TVs? obsolete equipment? — we re-purpose
              <br />
              your 'junk' from being yet <strong>another</strong> reason a
              turtle
              <br />
              chokes to death in its natural habbitat.
            </p>
          </article>
          <div className="div_getStarted">
            <a className="getStarted" href={"/signup"}>
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
