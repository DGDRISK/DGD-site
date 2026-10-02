import os, random, shutil
S=os.path.dirname(os.path.abspath(__file__))
PROD='/mnt/project-files/site/public'  # upload this folder to Netlify
ART=os.path.join(S,'..','site-artifact')  # preview copy (optional)
os.makedirs(PROD,exist_ok=True); os.makedirs(ART,exist_ok=True)

PHONE_DISPLAY='(916) 730-1954'; PHONE_TEL='+19167301954'
EMAIL='Delac.dgd@gmail.com'  # PENDING: switch to @dgdrisk.com address

FONTS='''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gloock&family=Montserrat:wght@600;800&family=Schibsted+Grotesk:wght@400;500;700&family=Martian+Mono:wght@400;600&display=swap">
<link rel="stylesheet" href="styles.css">'''

def header(active):
    cur=lambda k:' aria-current="page"' if k==active else ''
    return f'''<a class="skip-link" href="#main">Skip to content</a>

<!-- ============ HEADER ============ -->
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="DGD Risk and Insurance Services, home">
      <!-- LOGO: final "Home Shield" mark (logo.svg); full lockup in logo-full.svg -->
      <img src="logo.svg" alt="" width="80" height="90">
      <span class="logo-text">DGD<small>Risk and Insurance Services LLC</small></span>
    </a>
    <nav class="nav-desktop" aria-label="Primary">
      <ul>
        <li><a href="index.html#services">Services</a></li>
        <li><a href="index.html#about">About<span class="long"> Daniel</span></a></li>
        <li><a href="contact.html"{cur("contact")}>Contact<span class="long"> us</span></a></li>
        <li><a class="btn btn-primary" href="quote.html"{cur("quote")}>Get a quote</a></li>
      </ul>
    </nav>
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
      <span class="logo-text">DGD<small>Risk and Insurance Services LLC</small></span>
      <p class="ph">[Office address PENDING]</p>
      <p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <nav class="footer-nav" aria-label="Footer">
      <p class="eyebrow">Explore</p>
      <ul>
        <li><a href="index.html#services">Services</a></li>
        <li><a href="index.html#about">About Daniel</a></li>
        <li><a href="quote.html">Get a quote</a></li>
        <li><a href="contact.html">Contact us</a></li>
        <li><a href="privacy.html">Privacy policy</a></li>
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
        <p class="eyebrow">Hard-to-insure homes · Wildfire zones</p>
        <!-- HEADLINE: owner's choice -->
        <h1 id="hero-title">Closing the coverage gap for <em>the hardest-to-insure homes.</em></h1>
        <p class="hero-lede">When many standard insurers say no, DGD opens the door to wholesale insurance markets most homeowners never see. Your home deserves coverage, and wholesale insurers are built for hard-to-insure and high-value homes, including in high wildfire-risk areas that retail insurers won't touch. You probably don't have to settle for coverage from the FAIR Plan.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="quote.html">Get a quote <span class="arrow" aria-hidden="true">→</span></a>
        </div>
      </div>
      <aside class="hero-aside" aria-label="Experience">
        <span class="num">40</span>
        <p>years in commercial utility risk management, including insurers in the U.S., London and Bermuda. Now focusing on clients in Northern California, including Truckee, Tahoe and Monterey County.</p>
      </aside>
    </div>
    {SCENE}
  </section>

  <!-- ============ CREDIBILITY STRIP ============ -->
  <section class="trust" aria-label="Credentials">
    <div class="wrap">
      <ul>
        <li><strong>One point of contact</strong><span>You work directly with Daniel Delac, start to finish</span></li>
        <li><strong>NorCal focus</strong><span>Including Truckee, Tahoe and Monterey County</span></li>
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
        <p>Many standard insurers have stopped writing new homeowners policies in much of California. We work the markets that still do, and find an insurer for your home, even in high wildfire-risk areas.</p>
      </div>
      <div class="services">
        <article class="service">
          <svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M5 19 20 6l15 13"/><path d="M9 16v18h22V16"/><path d="M17 34v-9h6v9"/></svg>
          <p class="tag">Property</p>
          <h3>Homeowners property</h3>
          <p>Dwelling, contents and loss-of-use coverage for homes other carriers have declined or non-renewed because of wildfire exposure.</p>
        </article>
        <article class="service">
          <svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><circle cx="20" cy="20" r="15"/><path d="M5 20h30"/><path d="M20 5c-5 5-5 25 0 30M20 5c5 5 5 25 0 30"/></svg>
          <p class="tag">Wholesale markets</p>
          <h3>Wholesale market access</h3>
          <p>Access to wholesale and specialty markets for hard-to-insure homes when standard carriers won't write.</p>
        </article>
        <article class="service">
          <svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M20 4 31 22h-6l8 12H7l8-12H9z"/><path d="M20 34v4"/></svg>
          <p class="tag">Loss prevention</p>
          <h3>Wildfire risk review</h3>
          <p>Practical mitigation guidance on roofs, vents and defensible space, drawn from loss-prevention experience, to make your home insurable and increase its wildfire resiliency.</p>
        </article>
      </div>
    </div>
  </section>

  <!-- ============ ADDITIONAL SERVICES (referral partners) ============ -->
  <section class="section extra" id="additional-services" aria-labelledby="extra-title">
    <div class="wrap extra-grid">
      <div class="extra-copy">
        <p class="eyebrow">Additional services</p>
        <h2 id="extra-title">Beyond the policy: making your home safer</h2>
        <p>Through trusted independent specialists, DGD can connect you with services that lower your home's wildfire risk.</p>
        <ul class="extra-list">
          <li><strong>Residential wildfire risk analysis</strong><span>An expert assessment of your home's exposure and the steps that matter most.</span></li>
          <li><strong>Physical risk mitigation</strong><span>Ember-resistant vents, roof and gutter upgrades, and defensible-space work.</span></li>
          <li><strong>Fire suppression systems</strong><span>Design and installation of exterior sprinkler and suppression systems.</span></li>
        </ul>
        <p class="extra-note">These services are provided by independent companies DGD refers you to, not by DGD.</p>
      </div>
      <figure class="extra-figure">
        <svg class="extra-art" viewBox="0 0 480 360" role="img" aria-label="Illustration: a home protected by a rooftop fire sprinkler system, with cleared defensible space and pines">
          <rect width="480" height="360" fill="#EFE7D8"/>
          <path d="M0 250C80 236 160 244 240 240S400 232 480 246V360H0z" fill="#D9D2C4"/>
          <path d="M60 300C150 284 330 284 420 300" fill="none" stroke="#B87345" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round"/>
          <g fill="#24483E"><path d="M40 252 58 200 76 252z"/><path d="M47 222 58 180 69 222z"/><path d="M412 254 434 190 456 254z"/><path d="M420 218 434 168 448 218z"/><path d="M380 256 394 214 408 256z"/></g>
          <path d="M150 262V178L240 112l90 66v84z" fill="#24483E"/>
          <path d="M128 186 240 104l112 82" fill="none" stroke="#1A352D" stroke-width="12" stroke-linejoin="round"/>
          <rect x="222" y="206" width="36" height="56" fill="#B87345"/>
          <rect x="170" y="196" width="34" height="30" fill="#F7F3EB"/><rect x="276" y="196" width="34" height="30" fill="#F7F3EB"/>
          <g stroke="#F7F3EB" stroke-width="3"><path d="M187 196v30M170 211h34M293 196v30M276 211h34"/></g>
          <g fill="#1A352D"><rect x="180" y="128" width="8" height="18"/><rect x="236" y="88" width="8" height="18"/><rect x="292" y="128" width="8" height="18"/></g>
          <g fill="none" stroke="#6FA3B5" stroke-width="3" stroke-linecap="round" opacity=".9">
            <path d="M184 126C170 100 150 92 130 96"/><path d="M184 126C198 98 214 92 232 94"/>
            <path d="M240 86C226 58 204 50 184 54"/><path d="M240 86C254 58 276 50 296 54"/>
            <path d="M296 126C282 98 266 92 248 94"/><path d="M296 126C310 100 330 92 350 96"/>
          </g>
          <g fill="#6FA3B5"><circle cx="134" cy="108" r="3"/><circle cx="152" cy="118" r="2.5"/><circle cx="190" cy="66" r="3"/><circle cx="292" cy="66" r="3"/><circle cx="346" cy="108" r="3"/><circle cx="326" cy="118" r="2.5"/></g>
        </svg>
      </figure>
    </div>
  </section>

  <!-- ============ ABOUT: letter from Daniel ============ -->
  <section class="section about" id="about" aria-labelledby="about-title">
    <div class="wrap about-grid">
      <div class="about-side">
        <p class="eyebrow">About Daniel</p>
        <h2 id="about-title">One point of contact. Start to finish.</h2>
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
        <p>I've spent 40 years in risk management, in commercial utility risk management and wildfire loss prevention. Today I put all of it to work for one kind of client: a homeowner who is having trouble finding homeowners insurance.</p>
        <p>When the major carriers say no, I look at your home the way an underwriter will, tell you plainly what would help, and take it to the wholesale and specialty markets that are still writing.</p>
        <p>You'll have my direct number and my email. When you have a question, you'll be asking the person who placed your policy.</p>
        <p>I look forward to working with you to find you the best possible coverage.</p>
        <p class="sign">Daniel Delac</p>
        <p class="sign-title">DGD Risk and Insurance Services, LLC</p>
      </article>
    </div>
  </section>

  <!-- ============ FINAL CTA ============ -->
  <section class="final" id="contact" aria-labelledby="final-title">
    <div class="wrap">
      <h2 id="final-title">Talk to Daniel <em>directly.</em></h2>
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
          <div class="f"><label for="q-phone">Phone <span class="req" aria-hidden="true">*</span></label><input id="q-phone" name="phone" type="tel" autocomplete="tel" maxlength="14" pattern="\(\d{{3}}\) \d{{3}}-\d{{4}}" placeholder="(916) 555-0123" title="10-digit phone number" required></div>
          <div class="f full"><label for="q-email">Email</label><input id="q-email" name="email" type="email" autocomplete="email"></div>
        </fieldset>

        <fieldset>
          <legend>The property</legend>
          <div class="f full"><label for="q-address">Property address</label><input id="q-address" name="address" autocomplete="street-address"></div>
          <div class="f"><label for="q-zip">ZIP code</label><input id="q-zip" name="zip" inputmode="numeric" autocomplete="postal-code" maxlength="5" pattern="[0-9]{{5}}" title="5-digit ZIP code"></div>
          <div class="f"><label for="q-sqft">Square footage</label><input id="q-sqft" name="square_feet" inputmode="numeric" pattern="[0-9,]{{3,7}}" placeholder="e.g. 2,400" aria-describedby="q-sqft-hint"><span class="hint" id="q-sqft-hint">Living area. An estimate is fine.</span></div>
          <div class="f"><label for="q-market">Market value</label><input id="q-market" name="market_value" inputmode="numeric" maxlength="14" pattern="\$[0-9]{{1,3}}(,[0-9]{{3}})*" placeholder="e.g. $1,250,000" title="Dollar amount" aria-describedby="q-market-hint"><span class="hint" id="q-market-hint">What the home would sell for today. An estimate is fine.</span></div>
          <fieldset class="f full use"><legend class="sub">How is the home used?</legend>
            <div class="checks">
              <label class="check" for="q-use-owner"><input id="q-use-owner" name="use_owner_occupied" type="checkbox" value="Owner occupied"><span>Owner occupied</span></label>
              <label class="check" for="q-use-rental"><input id="q-use-rental" name="use_rental" type="checkbox" value="Rental"><span>Rental</span></label>
              <label class="check" for="q-use-vacation"><input id="q-use-vacation" name="use_vacation" type="checkbox" value="Vacation home"><span>Vacation home</span></label>
            </div>
            <span class="hint">Check all that apply.</span>
          </fieldset>
          <div class="f full"><label for="q-notes">Anything else we should know?</label><textarea id="q-notes" name="notes" placeholder="Mitigation work done, prior claims, coverage you want to keep"></textarea></div>
        </fieldset>

        <label class="check" for="q-consent"><input id="q-consent" name="consent" type="checkbox"><span>I agree that DGD Risk and Insurance Services may contact me by phone, text or email about my request. Consent is not a condition of purchase. See our <a href="privacy.html" target="_blank" rel="noopener">privacy policy</a>.</span></label>

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
  function digits(el,max){{ return el.value.replace(/\D/g,'').slice(0,max); }}
  var zip=document.getElementById('q-zip'), phone=document.getElementById('q-phone'), market=document.getElementById('q-market');
  zip.addEventListener('input',function(){{ zip.value=digits(zip,5); }});
  phone.addEventListener('input',function(){{
    var d=phone.value.replace(/\D/g,''); d=d.replace(/^1/,''); // US area codes never start with 1, so drop a typed +1 d=d.slice(0,10);
    phone.value=d.length>6?'('+d.slice(0,3)+') '+d.slice(3,6)+'-'+d.slice(6):d.length>3?'('+d.slice(0,3)+') '+d.slice(3):d;
  }});
  market.addEventListener('input',function(){{ var d=digits(market,10); market.value=d?'$'+Number(d).toLocaleString('en-US'):''; }});
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

PRIVACY=f'''{header("privacy")}

<main id="main">
  <section class="page-head dark" aria-labelledby="p-title">
    <div class="wrap">
      <p class="eyebrow" style="color:var(--on-dark-muted)">Legal</p>
      <h1 id="p-title">Privacy policy.</h1>
      <p>How DGD Risk and Insurance Services collects, uses, shares and protects your personal information.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap legal">
      <p class="ph"><strong>Effective date: [PENDING].</strong> Draft for review by DGD and its legal counsel before publication.</p>

      <h2>1. Who we are and what this policy covers</h2>
      <p>DGD Risk and Insurance Services, LLC ("DGD," "we," "us") is an insurance brokerage based in California. Daniel Delac is the firm's licensed broker. This policy explains how we handle personal information we collect through this website (dgdrisk.com), by phone, text and email, and in the course of finding, placing and servicing insurance for you. It is also our notice of information practices under the California Insurance Information and Privacy Protection Act (California Insurance Code sections 791 and following).</p>
      <p>By using this website or giving us information, you acknowledge this policy. If you do not agree with it, please do not submit information through the site and contact us by phone instead.</p>

      <h2>2. Information we collect</h2>
      <h3>Information you give us</h3>
      <ul>
        <li><strong>Contact details:</strong> name, phone number, email address.</li>
        <li><strong>Property details:</strong> property address and ZIP code, square footage, estimated market value, how the home is used (owner occupied, rental or vacation home), and anything you tell us in the comments box.</li>
        <li><strong>Insurance details</strong> you share by phone, email or in documents: current and prior policies, declarations pages, non-renewal or cancellation notices, renewal dates, prior claims, and wildfire mitigation work.</li>
        <li><strong>Application information</strong> an insurer requires to quote or issue a policy, which may include dates of birth, information about other household members, mortgage or lender details, and payment information.</li>
      </ul>
      <h3>Information from other sources</h3>
      <p>To obtain quotes and place coverage, we and the insurers we work with may receive information about you or your property from:</p>
      <ul>
        <li>insurance companies, wholesale brokers and surplus lines brokers;</li>
        <li>insurance-support organizations, such as databases of prior insurance claims;</li>
        <li>property inspection, replacement-cost and wildfire risk scoring services;</li>
        <li>public records, such as property and permit records;</li>
        <li>consumer reporting agencies, where permitted by law.</li>
      </ul>
      <h3>Information collected automatically</h3>
      <p>Our website is hosted by Netlify, Inc. Like most web hosts, Netlify automatically records technical information when you visit, such as your IP address, browser type, the pages you request and the date and time of your visit. These records are used to operate and secure the site. The site loads fonts from Google Fonts, which receives your IP address and browser information when a page loads.</p>
      <p>We do not use advertising cookies, analytics trackers or social media tracking pixels on this website. Because we do not track you across other websites, we do not respond differently to browser "Do Not Track" signals.</p>

      <h2>3. How we use your information</h2>
      <ul>
        <li>to respond to your request and contact you about it;</li>
        <li>to assess your insurance needs and your property's risk;</li>
        <li>to request quotes from, and submit applications to, insurers and wholesale or surplus lines brokers;</li>
        <li>to place, renew and service your policy and help you with claims;</li>
        <li>to suggest loss-prevention and wildfire mitigation steps;</li>
        <li>to keep business records and meet our legal, regulatory and licensing obligations;</li>
        <li>to detect and prevent fraud and to protect our rights and the security of our website.</li>
      </ul>

      <h2>4. How we share your information</h2>
      <p>We share personal information only as needed for the purposes above, with:</p>
      <ul>
        <li><strong>Insurers and other insurance intermediaries</strong>, including wholesale brokers and surplus lines brokers, so they can quote, underwrite, issue and service your coverage. Their own privacy notices govern how they use your information.</li>
        <li><strong>Service providers</strong> who help us run our business, such as our website and form host (Netlify) and our email provider, under obligations to use the information only to provide their services to us.</li>
        <li><strong>Government authorities and regulators</strong>, including the California Department of Insurance, when required by law, subpoena or court order, or to report suspected insurance fraud.</li>
        <li><strong>Others with your consent</strong>, such as your mortgage lender or a family member you authorize.</li>
        <li><strong>A successor</strong>, if DGD's business is sold, merged or transferred, subject to this policy.</li>
      </ul>
      <p><strong>We do not sell your personal information, and we do not share it for targeted advertising.</strong> We do not share nonpublic personal information with companies outside DGD for their own marketing. Except as the law permits without consent (for example, to process your insurance transaction), we will not disclose your nonpublic personal information to nonaffiliated third parties without your consent, as required by the California Financial Information Privacy Act.</p>

      <h2>5. Insurance information practices</h2>
      <ul>
        <li><strong>Pretext interviews.</strong> We do not use pretext interviews, meaning we do not pretend to be someone else to obtain information about you.</li>
        <li><strong>Investigative consumer reports.</strong> An insurer considering your application may request an investigative consumer report. If so, you may ask to be interviewed in connection with that report and to receive a copy of it.</li>
        <li><strong>Information disclosed without your authorization.</strong> Information we or an insurer collect may be disclosed to others without your prior authorization only in the circumstances California Insurance Code section 791.13 allows.</li>
      </ul>

      <h2>6. Your rights</h2>
      <h3>Access and correction</h3>
      <p>Under California insurance privacy law, you may ask in writing to see the recorded personal information we hold about you, to learn who it has been disclosed to, and to have inaccurate information corrected, amended or deleted. We will respond within 30 business days. If we decline to make a correction, you may submit a statement explaining why you disagree, which we will keep with your file and share with anyone who receives the disputed information.</p>
      <h3>Adverse underwriting decisions</h3>
      <p>If an insurer declines, cancels, non-renews or charges more for coverage based on information about you, you may ask for the specific reasons in writing and for a summary of your rights.</p>
      <h3>California Consumer Privacy Act</h3>
      <p>Much of the information we handle is governed by the federal Gramm-Leach-Bliley Act and California insurance privacy laws rather than the California Consumer Privacy Act (CCPA). To the extent the CCPA applies to DGD and to your information, you may request to know what personal information we have collected about you, to delete it, and to correct it, and you will not be treated differently for using these rights. You may make a request yourself or through an authorized agent. We will verify your identity before responding.</p>
      <h3>"Shine the Light"</h3>
      <p>We do not disclose personal information to third parties for their direct marketing purposes.</p>
      <p>To use any of these rights, contact us as shown in section 12.</p>

      <h2>7. Calls, texts and email</h2>
      <p>When you check the consent box on our quote form, you agree that DGD may contact you about your request by phone call, text message or email at the contact details you provided, including by automated means. Consent is not a condition of purchase. Message and data rates may apply. You can withdraw consent at any time by replying STOP to a text, asking us to stop when we call, or emailing us.</p>

      <h2>8. How we protect your information</h2>
      <p>We use reasonable administrative, technical and physical safeguards, appropriate to a small firm and to the sensitivity of the information, to protect personal information from unauthorized access, use and disclosure. Website traffic is encrypted with HTTPS. No method of transmission or storage is completely secure, so please do not send Social Security numbers, bank account or card numbers through the website form or ordinary email. Call us and we will arrange a secure way to share them.</p>

      <h2>9. How long we keep information</h2>
      <p>We keep personal information for as long as needed to respond to you, place and service your insurance, and resolve disputes, and for at least as long as California insurance record-keeping rules require. When information is no longer needed, we delete or securely dispose of it.</p>

      <h2>10. Children</h2>
      <p>This website is not directed to children under 16, and we do not knowingly collect personal information from them.</p>

      <h2>11. Changes to this policy</h2>
      <p>We may update this policy from time to time. We will post the new version on this page with a new effective date. If we make material changes to how we share personal information, we will give any notice the law requires.</p>

      <h2>12. Contact us</h2>
      <p>DGD Risk and Insurance Services, LLC<br>Attn: Daniel Delac<br><span class="ph">[Office address PENDING]</span><br>Phone: <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p>If you have a concern we have not resolved, you may contact the California Department of Insurance Consumer Hotline at 1-800-927-4357 or insurance.ca.gov.</p>
    </div>
  </section>
</main>

{FAB}

{FOOTER}'''

CONTACT=f'''{header("contact")}

<main id="main">
  <section class="page-head dark" aria-labelledby="c-title">
    <div class="wrap">
      <p class="eyebrow" style="color:var(--on-dark-muted)">Contact us</p>
      <h1 id="c-title">Talk to Daniel.</h1>
      <p>Questions about your coverage, a non-renewal notice or the FAIR Plan? Reach Daniel directly. No call center, no hand-offs.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap form-layout">
      <form class="quote-form contact-form" name="contact" method="POST" action="/thanks.html" data-netlify="true" data-netlify-honeypot="bot-field">
        <input type="hidden" name="form-name" value="contact">
        <p hidden><label>Leave this empty: <input name="bot-field"></label></p>
        <p class="hint req-note"><span class="req" aria-hidden="true">*</span> Name and phone are required.</p>
        <fieldset>
          <legend>Send a message</legend>
          <div class="f"><label for="c-name">Name <span class="req" aria-hidden="true">*</span></label><input id="c-name" name="name" autocomplete="name" required></div>
          <div class="f"><label for="c-phone">Phone <span class="req" aria-hidden="true">*</span></label><input id="c-phone" name="phone" type="tel" autocomplete="tel" required></div>
          <div class="f full"><label for="c-email">Email</label><input id="c-email" name="email" type="email" autocomplete="email"></div>
          <div class="f full"><label for="c-msg">How can Daniel help?</label><textarea id="c-msg" name="message"></textarea></div>
        </fieldset>
        <label class="check" for="c-consent"><input id="c-consent" name="consent" type="checkbox"><span>I agree that DGD Risk and Insurance Services may contact me by phone, text or email about my message. Consent is not a condition of purchase. See our <a href="privacy.html" target="_blank" rel="noopener">privacy policy</a>.</span></label>
        <div><button class="btn btn-primary" type="submit">Send message <span class="arrow" aria-hidden="true">→</span></button></div>
      </form>

      <aside class="form-aside" aria-label="Contact details">
        <div class="aside-block">
          <h2>Call</h2>
          <p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
        </div>
        <div class="aside-block">
          <h2>Email</h2>
          <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        </div>
        <div class="aside-block">
          <h2>Office</h2>
          <p class="ph">[Office address PENDING]</p>
        </div>
        <div class="aside-block">
          <h2>Need a quote?</h2>
          <p><a href="quote.html">Use the quote form</a> to send your property details.</p>
        </div>
      </aside>
    </div>
  </section>
</main>

{FAB}

{FOOTER}'''

THANKS=f'''{header("thanks")}

<main id="main">
  <section class="page-head dark" aria-labelledby="t-title">
    <div class="wrap">
      <p class="eyebrow" style="color:var(--on-dark-muted)">Message sent</p>
      <h1 id="t-title">Thank you.</h1>
      <p>Daniel will get back to you, usually within one business day. If it's urgent, call <a href="tel:{PHONE_TEL}" style="color:inherit">{PHONE_DISPLAY}</a>.</p>
      <p><a class="btn btn-primary" href="index.html">Back to home</a></p>
    </div>
  </section>
</main>

{FOOTER}'''

META={'index':('DGD Risk and Insurance Services | Hard-to-Insure Homes in Wildfire Areas','Homeowners insurance for hard-to-insure homes in high wildfire-risk areas, including Truckee, Tahoe and Monterey County. Wholesale and specialty market access.'),
      'quote':('Get a Quote | DGD Risk and Insurance Services','Request a homeowners insurance quote for a hard-to-insure home in Northern California.'),
      'contact':('Contact Us | DGD Risk and Insurance Services','Contact Daniel Delac at DGD Risk and Insurance Services about homeowners insurance for hard-to-insure homes.'),
      'thanks':('Thank You | DGD Risk and Insurance Services','Your message was sent.'),
      'privacy':('Privacy Policy | DGD Risk and Insurance Services','How DGD Risk and Insurance Services collects, uses, shares and protects personal information.')}

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
for n,b in (('index',INDEX),('quote',QUOTE),('privacy',PRIVACY),('contact',CONTACT),('thanks',THANKS)):
    open(f'{PROD}/{n}.html','w').write(full(n,b))
for f in ('styles.css','logo.svg','logo-full.svg'):
    shutil.copy(os.path.join(S,f),PROD); shutil.copy(os.path.join(S,f),ART)
# artifact: main page without document skeleton; quote.html as full page
open(f'{ART}/index.html','w').write(f'<title>DGD Tahoe Site</title>\n{FONTS}\n{INDEX}')
open(f'{ART}/quote.html','w').write(full('quote',QUOTE))
print('built')
