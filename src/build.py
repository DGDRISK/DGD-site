import os, random, shutil
S=os.path.dirname(os.path.abspath(__file__))
PROD='/mnt/project-files/site/public'  # upload this folder to Netlify
ART=os.path.join(S,'..','site-artifact')  # preview copy (optional)
os.makedirs(PROD,exist_ok=True); os.makedirs(ART,exist_ok=True)

PHONE_DISPLAY='(916) 730-1954'; PHONE_TEL='+19167301954'
EMAIL='Delac.dgd@gmail.com'  # PENDING: switch to @dgdrisk.com address

FONTS='''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gloock&family=Schibsted+Grotesk:wght@400;500;700&family=Martian+Mono:wght@400;600&display=swap">
<link rel="stylesheet" href="styles.css">'''

def header(active):
    cur=lambda k:' aria-current="page"' if k==active else ''
    return f'''<a class="skip-link" href="#main">Skip to content</a>

<!-- ============ HEADER ============ -->
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="DGD Risk and Insurance Services, home">
      <!-- LOGO: PROVISIONAL "Home in the Pines" mark (logo.svg); full lockup in logo-full.svg -->
      <img src="logo.svg" alt="" width="44" height="44">
      <span class="logo-text">DGD<small>Risk and Insurance Services</small></span>
    </a>
    <nav class="nav-desktop" aria-label="Primary">
      <ul>
        <li><a href="index.html#services">Services</a></li>
        <li><a href="index.html#about">About Daniel</a></li>
        <li><a href="index.html#how">How it works</a></li>
        <li><a href="mailto:{EMAIL}">Email us</a></li>
        <li><a class="btn btn-primary" href="quote.html"{cur("quote")}>Get a quote</a></li>
      </ul>
    </nav>
    <details class="nav-mobile">
      <summary>Menu</summary>
      <nav aria-label="Primary mobile">
        <ul>
          <li><a href="index.html#services">Services</a></li>
          <li><a href="index.html#about">About Daniel</a></li>
          <li><a href="index.html#how">How it works</a></li>
          <li><a href="index.html#reviews">Reviews</a></li>
          <li><a href="quote.html">Get a quote</a></li>
          <li><a href="mailto:{EMAIL}">Email us</a></li>
        </ul>
      </nav>
    </details>
  </div>
</header>'''

FAB='''<!-- Floating quote button (hidden on the quote page) -->
<a class="fab" href="quote.html" aria-label="Get a quote">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h5"/></svg>
  <span>Get a quote</span>
</a>'''

FOOTER=f'''<!-- ============ FOOTER ============ -->
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-brand">
      <span class="logo-text">DGD<small>Risk and Insurance Services</small></span>
      <p class="ph">[Office address PENDING]</p>
      <p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <nav class="footer-nav" aria-label="Footer">
      <p class="eyebrow">Explore</p>
      <ul>
        <li><a href="index.html#services">Services</a></li>
        <li><a href="index.html#about">About Daniel</a></li>
        <li><a href="index.html#how">How it works</a></li>
        <li><a href="quote.html">Get a quote</a></li>
        <li><a href="index.html#top" class="ph">Privacy policy (PENDING)</a></li>
      </ul>
    </nav>
    <!-- DISCLAIMER: TEMPLATE TEXT, PENDING compliance and legal review -->
    <div class="footer-legal">
      <p><strong class="ph">License #[PENDING]</strong></p>
      <p class="ph">DGD Risk and Insurance Services, LLC is a licensed insurance brokerage. Information on this website is for general informational purposes only and is not an offer of insurance, a binder, or a guarantee of coverage. All coverage is subject to underwriting approval and to the terms, conditions and exclusions of the policy issued. Availability, carriers and pricing vary by property, location and market conditions. Some policies may be placed with non-admitted (surplus lines) insurers, which are not licensed by the state, are subject to limited state regulatory oversight, and are not protected by the state insurance guaranty fund. Submitting a request does not bind coverage; no coverage is in force until confirmed in writing.</p>
    </div>
    <div class="footer-base">
      <span>© 2026 DGD Risk and Insurance Services, LLC</span>
      <span>Coverage is subject to underwriting approval.</span>
    </div>
  </div>
</footer>'''

# ---------- Tahoe dusk scene (illustration; swap for a licensed photo later) ----------
random.seed(7)
def pines(xs, ybase, hmin, hmax, fill):
    out=[]
    for x in xs:
        h=random.randint(hmin,hmax); w=h*0.4
        out.append(f'<use href="#pine" x="{x-w/2:.0f}" y="{ybase-h}" width="{w:.0f}" height="{h}" fill="{fill}"/>')
    return '\n    '.join(out)
far=pines(range(0,1460,26),352,26,48,'#7F998C')
near_left=pines([20,70,115,170,230,290,350,420,480,540,610,680,740,790],470,90,170,'#24483E')
near_right=pines([840,880,1220,1265,1310,1355,1400,1440],470,110,190,'#24483E')
SCENE=f'''<svg class="scene" viewBox="0 0 1440 520" preserveAspectRatio="xMaxYMax slice" aria-hidden="true" focusable="false">
  <defs>
    <symbol id="pine" viewBox="0 0 40 100"><path d="M20 0 31 28h-5l9 24h-6l11 30H0l11-30H5l9-24H9z"/><rect x="18" y="82" width="4" height="18"/></symbol>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#E9B65A" stop-opacity=".45"/><stop offset="1" stop-color="#E9B65A" stop-opacity="0"/></radialGradient>
    <linearGradient id="lake" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E3EAE5"/><stop offset="1" stop-color="#C7D5CD"/></linearGradient>
  </defs>
  <!-- distant granite ridges -->
  <path d="M0 300 110 250 210 272 330 196 430 248 540 222 690 150 790 210 930 182 1060 236 1190 176 1310 226 1440 200V520H0z" fill="#D6DDD4"/>
  <path d="M640 168 690 150 742 180 712 176 690 166 668 180z M1160 190 1190 176 1222 198 1196 194z" fill="#FFFFFF" opacity=".8"/>
  <path d="M0 350 150 316 300 340 470 298 640 334 820 306 1000 340 1170 306 1320 332 1440 316V520H0z" fill="#AFC0B5"/>
  {''}<g>
    {far}
  </g>
  <!-- the lake -->
  <rect x="0" y="352" width="1440" height="80" fill="url(#lake)"/>
  <g stroke="#FFFFFF" stroke-width="2" opacity=".8"><path d="M120 372h140M420 390h200M760 378h120M1000 398h90M300 412h110"/></g>
  <!-- lodge reflection -->
  <rect x="955" y="410" width="190" height="18" fill="#B87345" opacity=".15"/>
  <!-- foreground shore -->
  <path d="M0 440C220 424 420 436 640 430S1100 420 1440 436V520H0z" fill="#24483E"/>
  <!-- the lodge -->
  
  <g>
    <path d="M915 444V382h270v62z" fill="#1A352D"/>
    <path d="M950 382 1050 290 1150 382z" fill="#24483E"/>
    <path d="M975 382 1050 314 1125 382z" fill="#D9A577"/>
    <path d="M1050 314V382M1012 382 1050 348 1088 382M1000 360h100" stroke="#1A352D" stroke-width="4" fill="none"/>
    <path d="M1150 394 1195 356 1240 394z" fill="#24483E"/>
    <path d="M1160 394h70v50h-70z" fill="#1A352D"/>
    <rect x="1170" y="404" width="50" height="28" fill="#D9A577"/>
    <rect x="932" y="396" width="56" height="34" fill="#D9A577"/>
    <rect x="1002" y="396" width="96" height="34" fill="#E6BE96"/>
    <rect x="1112" y="396" width="56" height="34" fill="#D9A577"/>
    <path d="M1030 396v34M1050 396v34M1070 396v34" stroke="#1A352D" stroke-width="3"/>
    <rect x="900" y="442" width="360" height="8" fill="#1A352D"/>
    <rect x="1090" y="262" width="16" height="40" fill="#1A352D"/>
  </g>
  <g>
    {near_left}
    {near_right}
  </g>
</svg>'''

STAR='<svg viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path d="m10 1.5 2.6 5.4 5.9.8-4.3 4.1 1 5.9L10 14.9l-5.2 2.8 1-5.9L1.5 7.7l5.9-.8z"/></svg>'
STARS=f'<div class="stars" role="img" aria-label="Rated 5 out of 5">{STAR*5}</div>'

INDEX=f'''{header("home")}

<main id="main">

  <!-- ============ HERO ============ -->
  <section class="hero" id="top" aria-labelledby="hero-title">
    <div class="wrap">
      <div class="hero-main">
        <p class="eyebrow">Northern California · Hard-to-insure homes</p>
        <!-- HEADLINE: PENDING owner's final choice (option 1 shown) -->
        <h1 id="hero-title">Closing the coverage gap in <em>Northern California's hardest-to-insure places.</em></h1>
        <p class="hero-lede">When the major carriers stop writing in Truckee, Tahoe, the South Bay hills or Monterey County, DGD goes to wholesale and specialty markets to place your property and liability coverage.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="quote.html">Get a quote <span class="arrow" aria-hidden="true">→</span></a>
          <a class="link-line" href="#how">See how it works</a>
        </div>
      </div>
      <aside class="hero-aside" aria-label="Experience">
        <span class="num">40</span>
        <p>years in risk management across the U.S., London and California. Now focused on Northern California.</p>
      </aside>
    </div>
    {SCENE}
  </section>

  <!-- ============ CREDIBILITY STRIP ============ -->
  <section class="trust" aria-label="Credentials">
    <div class="wrap">
      <ul>
        <li><strong>40 years</strong><span>Risk management experience</span></li>
        <li><strong>One broker</strong><span>You work directly with Daniel Delac, start to finish</span></li>
        <li><strong>NorCal focus</strong><span>Truckee, Tahoe, the South Bay and Monterey County</span></li>
        <li><strong class="ph">License #</strong><span class="ph">Number and states PENDING</span></li>
      </ul>
    </div>
  </section>

  <!-- ============ SERVICES ============ -->
  <section class="section" id="services" aria-labelledby="services-title">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">What we do</p>
        <h2 id="services-title">Coverage where the major carriers pulled back</h2>
        <p>Standard carriers have stopped writing new homeowners policies in much of Northern California. We work the markets that still do, and help your home become a risk they want.</p>
      </div>
      <div class="services">
        <article class="service">
          <svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M5 19 20 6l15 13"/><path d="M9 16v18h22V16"/><path d="M17 34v-9h6v9"/></svg>
          <p class="tag">Property</p>
          <h3>Homeowners property</h3>
          <p>Dwelling, contents and loss-of-use coverage for homes other carriers have declined or non-renewed because of wildfire exposure.</p>
        </article>
        <article class="service">
          <svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M20 4 7 9v10c0 8 6 14 13 17 7-3 13-9 13-17V9z"/><path d="m14 20 4 4 8-9"/></svg>
          <p class="tag">Liability</p>
          <h3>Personal liability</h3>
          <p>Liability protection placed alongside your property coverage, so a hard-to-place home doesn't leave you exposed elsewhere.</p>
        </article>
        <article class="service">
          <svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><circle cx="20" cy="20" r="15"/><path d="M5 20h30"/><path d="M20 5c-5 5-5 25 0 30M20 5c5 5 5 25 0 30"/></svg>
          <p class="tag">Wholesale markets</p>
          <h3>Wholesale market access</h3>
          <p>Access to wholesale and specialty markets for hard-to-insure homes in Northern California, when standard carriers won't write.</p>
        </article>
        <article class="service">
          <svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M20 4 31 22h-6l8 12H7l8-12H9z"/><path d="M20 34v4"/></svg>
          <p class="tag">Loss prevention</p>
          <h3>Wildfire risk review</h3>
          <p>Practical mitigation guidance on roofs, vents and defensible space, drawn from loss-prevention experience, so underwriters see a better risk.</p>
        </article>
      </div>
    </div>
  </section>

  <!-- ============ ABOUT: letter from Daniel ============ -->
  <section class="section about" id="about" aria-labelledby="about-title">
    <div class="wrap about-grid">
      <div class="about-side">
        <p class="eyebrow">About Daniel</p>
        <h2 id="about-title">One broker. Start to finish.</h2>
        <!-- PHOTO: replace with <img src="daniel.jpg" alt="Daniel Delac" width="480" height="600"> -->
        <div class="portrait ph" role="img" aria-label="Photo of Daniel Delac (pending)"><span>Photo of Daniel<br>PENDING</span></div>
        <ul class="promise">
          <li><strong>You reach Daniel.</strong> No call center, no phone tree, no hand-offs.</li>
          <li><strong>The same person at every step.</strong> First call, placement, every renewal.</li>
          <li><strong>A direct line.</strong> <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
        </ul>
      </div>
      <article class="letter">
        <p class="salute">Dear homeowner,</p>
        <p>When you call DGD Risk and Insurance Services, you reach me. Not a call center, not an assistant, and not a junior agent learning on your file. DGD is a one-person firm by design, and I handle every client personally, from the first conversation to the day your coverage is bound and every renewal after that.</p>
        <p>I've spent 40 years in risk management, in corporate risk, agency work and wildfire loss prevention, across the United States, London and California. Today I put all of it to work for one kind of client: Northern California homeowners in Truckee, Tahoe, the South Bay and Monterey County whose homes have become hard to insure.</p>
        <p>When the major carriers say no, I look at your home the way an underwriter will, tell you plainly what would help, and take it to the wholesale and specialty markets that are still writing.</p>
        <p>You'll have my direct number and my email. When you have a question, you'll be asking the person who placed your policy.</p>
        <p class="sign">Daniel Delac</p>
        <p class="sign-title">DGD Risk and Insurance Services, LLC</p>
      </article>
    </div>
  </section>

  <!-- ============ HOW IT WORKS ============ -->
  <section class="section how dark" id="how" aria-labelledby="how-title">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">How it works</p>
        <h2 id="how-title">Three steps to coverage</h2>
        <p>Start at least 60 days before your renewal date if you can. More time means more markets to approach.</p>
      </div>
      <ol class="steps">
        <li><h3>Send your details</h3><p>Fill out the <a class="link-line" href="quote.html">quote form</a> with your address and your non-renewal notice or current declarations page.</p></li>
        <li><h3>We assess and shop</h3><p>We review your wildfire exposure, suggest mitigation that improves your odds, and approach the markets that fit.</p></li>
        <li><h3>Choose and bind</h3><p>You get your options in plain language, including how each carrier is regulated, then pick the one that fits.</p></li>
      </ol>
    </div>
  </section>

  <!-- ============ TESTIMONIALS (PENDING: real reviews with written permission) ============ -->
  <section class="section" id="reviews" aria-labelledby="reviews-title">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Client reviews</p>
        <h2 id="reviews-title">Homeowners we've placed</h2>
        <p>Every review comes from a real client and is shared with their permission.</p>
      </div>
      <div class="reviews">
        <figure class="review ph">{STARS}
          <blockquote><p>[PENDING review] A client whose carrier non-renewed them, in their own words: what happened and how it was resolved.</p></blockquote>
          <figcaption>[First name, initial] · [Town]</figcaption></figure>
        <figure class="review ph">{STARS}
          <blockquote><p>[PENDING review] A short quote about the mitigation advice or how clearly the options were explained.</p></blockquote>
          <figcaption>[First name, initial] · [Town]</figcaption></figure>
        <figure class="review ph">{STARS}
          <blockquote><p>[PENDING review] A client in Truckee, Tahoe, the South Bay or Monterey County whose home was hard to place.</p></blockquote>
          <figcaption>[First name, initial] · [Town]</figcaption></figure>
      </div>
      <p class="review-note">Individual results vary. Coverage availability depends on underwriting.</p>
    </div>
  </section>

  <!-- ============ FINAL CTA ============ -->
  <section class="final" id="contact" aria-labelledby="final-title">
    <div class="wrap">
      <h2 id="final-title">Your renewal date <em>is the deadline.</em></h2>
      <div class="final-body">
        <p>Send your non-renewal notice or declarations page. Daniel will review it personally and tell you where you stand and which markets to approach.</p>
        <a class="btn btn-primary" href="quote.html">Get a quote <span class="arrow" aria-hidden="true">→</span></a>
        <div class="contact-lines">
          <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
          <a href="mailto:{EMAIL}">{EMAIL}</a>
        </div>
      </div>
    </div>
  </section>
</main>

{FAB}

{FOOTER}'''

QUOTE=f'''{header("quote")}

<main id="main">
  <section class="page-head dark" aria-labelledby="q-title">
    <div class="wrap">
      <p class="eyebrow" style="color:var(--on-dark-muted)">Get a quote</p>
      <h1 id="q-title">Tell us about your home.</h1>
      <p>It takes about three minutes. We'll review your property and reply with your options, usually within one business day.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap form-layout">
      <!-- FORM: handled by Netlify Forms (form detection must be enabled in Netlify: Site configuration > Forms) -->
      <form class="quote-form" id="quote-form" name="quote" method="POST" action="/" enctype="multipart/form-data" data-netlify="true" data-netlify-honeypot="bot-field" novalidate>
        <input type="hidden" name="form-name" value="quote">
        <p hidden><label>Leave this empty: <input name="bot-field"></label></p>
        <p class="hint req-note"><span class="req" aria-hidden="true">*</span> Only name and phone are required. Everything else helps but is optional.</p>
        <fieldset>
          <legend>Owner</legend>
          <div class="f"><label for="q-name">Owner name <span class="req" aria-hidden="true">*</span></label><input id="q-name" name="name" autocomplete="name" required></div>
          <div class="f"><label for="q-phone">Phone <span class="req" aria-hidden="true">*</span></label><input id="q-phone" name="phone" type="tel" autocomplete="tel" required></div>
          <div class="f full"><label for="q-email">Email</label><input id="q-email" name="email" type="email" autocomplete="email"></div>
        </fieldset>

        <fieldset>
          <legend>The property</legend>
          <div class="f full"><label for="q-address">Property address</label><input id="q-address" name="address" autocomplete="street-address"></div>
          <div class="f"><label for="q-zip">ZIP code</label><input id="q-zip" name="zip" inputmode="numeric" autocomplete="postal-code" pattern="[0-9]{{5}}"></div>
          <div class="f"><label for="q-sqft">Square footage</label><input id="q-sqft" name="square_feet" inputmode="numeric" pattern="[0-9,]{{3,7}}" placeholder="e.g. 2,400" aria-describedby="q-sqft-hint"><span class="hint" id="q-sqft-hint">Living area. An estimate is fine.</span></div>
          <div class="f"><label for="q-market">Market value</label><input id="q-market" name="market_value" inputmode="numeric" pattern="\$?[0-9,]{{5,12}}" placeholder="e.g. $1,250,000" aria-describedby="q-market-hint"><span class="hint" id="q-market-hint">What the home would sell for today. An estimate is fine.</span></div>
          <fieldset class="f full use"><legend class="sub">How is the home used?</legend>
            <div class="checks">
              <label class="check" for="q-use-owner"><input id="q-use-owner" name="use_owner_occupied" type="checkbox" value="Owner occupied"><span>Owner occupied</span></label>
              <label class="check" for="q-use-rental"><input id="q-use-rental" name="use_rental" type="checkbox" value="Rental"><span>Rental</span></label>
              <label class="check" for="q-use-vacation"><input id="q-use-vacation" name="use_vacation" type="checkbox" value="Vacation home"><span>Vacation home</span></label>
            </div>
            <span class="hint">Check all that apply.</span>
          </fieldset>
          <div class="f"><label for="q-status">Current situation</label>
            <select id="q-status" name="status">
              <option value="">Choose one</option>
              <option>Received a non-renewal or cancellation</option>
              <option>Currently on the FAIR Plan</option>
              <option>Premium went up sharply</option>
              <option>Buying a home</option>
              <option>Other</option>
            </select></div>
          <div class="f"><label for="q-renewal">Renewal or closing date</label><input id="q-renewal" name="renewal_date" type="date"></div>
          <div class="f"><label for="q-roof">Roof type</label>
            <select id="q-roof" name="roof">
              <option value="">Choose one</option>
              <option>Metal</option><option>Tile or concrete</option><option>Composition shingle</option><option>Wood shake</option><option>Not sure</option>
            </select></div>
          <div class="f"><label for="q-built">Year built</label><input id="q-built" name="year_built" inputmode="numeric" pattern="[0-9]{{4}}"></div>
          <div class="f full"><label for="q-file">Non-renewal notice or declarations page</label><input id="q-file" name="document" type="file" accept=".pdf,.jpg,.jpeg,.png,.heic"><span class="hint">PDF or photo. Optional, but it speeds things up.</span></div>
          <div class="f full"><label for="q-notes">Anything else we should know?</label><textarea id="q-notes" name="notes" placeholder="Mitigation work done, prior claims, coverage you want to keep"></textarea></div>
        </fieldset>

        <label class="check" for="q-consent"><input id="q-consent" name="consent" type="checkbox"><span>I agree that DGD Risk and Insurance Services may contact me by phone, text or email about my request. Consent is not a condition of purchase. <span class="ph">See our privacy policy (PENDING).</span></span></label>

        <div><button class="btn btn-primary" type="submit">Send my request <span class="arrow" aria-hidden="true">→</span></button></div>
        <div class="form-status" id="form-status" role="status" aria-live="polite" hidden></div>
        <p class="eyebrow">Submitting this form does not bind coverage.</p>
      </form>

      <aside class="form-aside" aria-label="Other ways to reach us">
        <div class="aside-block">
          <h2>Rather talk?</h2>
          <p>Call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br>or email <a href="mailto:{EMAIL}">{EMAIL}</a></p>
        </div>
        <div class="aside-block">
          <h2>Have these handy</h2>
          <ul>
            <li>Your non-renewal or cancellation notice</li>
            <li>Current declarations page</li>
            <li>Roof age and material</li>
            <li>Any mitigation work: vents, defensible space, ember-resistant upgrades</li>
          </ul>
        </div>
      </aside>
    </div>
  </section>
</main>

{FOOTER}

<script>
/* Quote form: native validation, then POST to Netlify Forms.
   Only submits on the live site (Netlify or dgdrisk.com); anywhere else it shows a call/email fallback. */
(function(){{
  var form=document.getElementById('quote-form'), status=document.getElementById('form-status');
  function show(msg,isError){{status.hidden=false;status.className='form-status'+(isError?' error':'');status.textContent=msg;}}
  form.addEventListener('submit',function(e){{
    e.preventDefault();
    if(!form.checkValidity()){{
      form.reportValidity();
      var first=form.querySelector(':invalid'); if(first) first.focus();
      return;
    }}
    var host=location.hostname, live=/netlify\.app$|dgdrisk\.com$/.test(host);
    if(!live){{
      show('This preview cannot send forms. Please call {PHONE_DISPLAY} or email {EMAIL} and we will get right back to you.',true);
      return;
    }}
    var btn=form.querySelector('button[type=submit]'); btn.disabled=true;
    var fd=new FormData(form);
    // iPhone Safari can fail the whole send when a file field is left empty, so drop empty file fields.
    Array.from(fd.entries()).forEach(function(e){{ if(e[1] instanceof File && !e[1].name && !e[1].size) fd.delete(e[0]); }});
    fetch('/',{{method:'POST',body:fd}})
      .then(function(r){{ if(!r.ok) throw new Error('status '+r.status); form.reset(); show('Thanks. Your request was sent. We will reply within one business day.'); }})
      .catch(function(err){{
        // Background send failed: let the browser post the form directly so Netlify handles it (and shows its own page).
        if(!form.dataset.retried){{ form.dataset.retried='1'; HTMLFormElement.prototype.submit.call(form); return; }}
        show('Your request could not be sent ('+(err&&err.message||'network')+'). Please call {PHONE_DISPLAY} or email {EMAIL}.',true);
      }})
      .finally(function(){{ btn.disabled=false; }});
  }});
}})();
</script>'''

META={'index':('DGD Risk and Insurance Services | Hard-to-Insure Homes in Northern California','Homeowners insurance for hard-to-insure homes in Northern California: Truckee, Tahoe, the South Bay and Monterey County. Wholesale and specialty market access.'),
      'quote':('Get a Quote | DGD Risk and Insurance Services','Request a homeowners insurance quote for a hard-to-insure home in Northern California.')}

def full(name,body):
    t,d=META[name]
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t}</title>
<meta name="description" content="{d}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta name="theme-color" content="#24483E">
<link rel="icon" href="logo.svg" type="image/svg+xml">
{FONTS}
</head>
<body>
{body}
</body>
</html>
'''
for n,b in (('index',INDEX),('quote',QUOTE)):
    open(f'{PROD}/{n}.html','w').write(full(n,b))
for f in ('styles.css','logo.svg','logo-full.svg'):
    shutil.copy(os.path.join(S,f),PROD); shutil.copy(os.path.join(S,f),ART)
# artifact: main page without document skeleton; quote.html as full page
open(f'{ART}/index.html','w').write(f'<title>DGD Tahoe Site</title>\n{FONTS}\n{INDEX}')
open(f'{ART}/quote.html','w').write(full('quote',QUOTE))
print('built')
