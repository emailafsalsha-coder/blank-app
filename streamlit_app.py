import streamlit as st
import streamlit.components.v1 as components

# Page config with SEO optimization
st.set_page_config(
    page_title="치지직 VOD 다운로더 - 무료 CHZZK 비디오 다운로드 도구",
    page_icon="https://www.chzzkdownloader.com/favicon.ico",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.chzzkdownloader.com/support',
        'Report a bug': "https://www.chzzkdownloader.com/report",
        'About': "# 치지직 VOD 다운로더\n가장 빠르고 안전한 CHZZK 비디오 다운로드 서비스"
    }
)

# SEO meta description
st.markdown("""
<meta name="description" content="무료 치지직 VOD 다운로더 - CHZZK 비디오를 빠르고 안전하게 다운로드하세요. 간단한 URL 입력으로 고품질 비디오 다운로드가 가능합니다.">
<meta name="keywords" content="치지직, CHZZK, VOD, 다운로더, 비디오 다운로드, 무료, 온라인 도구">
<meta name="author" content="CHZZK Save">
<meta property="og:title" content="치지직 VOD 다운로더 - 무료 CHZZK 비디오 다운로드">
<meta property="og:description" content="가장 빠르고 안전한 CHZZK 비디오 다운로드 서비스. 간단한 URL로 고품질 VOD를 무료로 다운로드하세요.">
<meta property="og:type" content="website">
<meta property="og:image" content="https://chzzkdownloader.com/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="치지직 VOD 다운로더">
<meta name="twitter:description" content="무료 CHZZK 비디오 다운로드 도구">
<meta name="robots" content="index, follow">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
""", unsafe_allow_html=True)

# Analytics scripts using components.html to execute JavaScript
components.html("""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-C7NC1BWTEG"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-C7NC1BWTEG');
</script>

<!-- Microsoft Clarity -->
<script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "YOUR_CLARITY_ID");
</script>
""", height=0)

# Premium purchase button
st.markdown("""
<a href="https://www.paypal.com/ncp/payment/LM7VS22YPJVKJ" target="_blank" class="premium-button">
    <span class="premium-icon">⭐</span>
    프리미엄 구매
</a>
""", unsafe_allow_html=True)

# Original CSS styling with scrolling fixes
st.markdown("""
<style>
    /* Global dark background */
    .stApp {
        background-color: #1a1a1a !important;
    }
    
    /* Hide Streamlit elements */
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    .stDecoration {display:none;}
    header {visibility: hidden;}
    
    /* Main container - removed height restrictions */
    .block-container {
        padding: 4rem 2rem 2rem 2rem !important;
        max-width: 800px !important;
        margin: 0 auto !important;
        min-height: 100vh !important;
    }
    
    /* Ensure main content is scrollable */
    .main > div {
        overflow-y: auto !important;
        height: auto !important;
    }
    
    /* Title styling - centered like in image */
    .main-title {
        color: #00d97a;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin: 2rem 0 4rem 0;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .link-icon {
        margin-right: 12px;
        font-size: 2.2rem;
    }
    
    /* Premium button styling */
    .premium-button {
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1000;
        background: linear-gradient(135deg, #ff6b6b, #ee5a24) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 10px 20px !important;
        text-decoration: none !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3) !important;
        transition: all 0.3s ease !important;
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
    }
    
    .premium-button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4) !important;
        text-decoration: none !important;
        color: white !important;
    }
    
    .premium-icon {
        font-size: 16px;
    }
    
    /* Input container - no visible borders */
    .input-section {
        max-width: 600px;
        margin: 0 auto;
        padding: 0;
    }
    
    /* VOD URL label styling */
    .stTextInput label {
        color: #888 !important;
        font-size: 14px !important;
        font-weight: 400 !important;
        margin-bottom: 8px !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Input field - exactly like original */
    .stTextInput > div > div > input {
        background-color: #2d2d2d !important;
        color: #ffffff !important;
        border: 1px solid #3a3a3a !important;
        border-radius: 8px !important;
        padding: 16px 18px !important;
        font-size: 16px !important;
        height: 56px !important;
        width: 100% !important;
        box-sizing: border-box !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #777 !important;
        font-style: italic;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #00d97a !important;
        box-shadow: 0 0 0 1px #00d97a !important;
        outline: none !important;
    }
    
    /* Button styling - original design */
    .stLinkButton > a {
        background-color: #2d2d2d !important;
        color: #ffffff !important;
        border: 1px solid #3a3a3a !important;
        border-radius: 8px !important;
        padding: 16px 24px !important;
        text-decoration: none !important;
        font-weight: 500 !important;
        font-size: 16px !important;
        display: block !important;
        text-align: center !important;
        margin-top: 24px !important;
        height: 56px !important;
        line-height: 24px !important;
        transition: all 0.2s ease !important;
    }
    
    .stLinkButton > a:hover {
        background-color: #373737 !important;
        border-color: #4a4a4a !important;
    }
    
    /* Age-restricted download link styling */
    .age-restricted-link {
        color: rgba(255, 255, 255, 0.8) !important;
        font-size: 14px !important;
        text-decoration: none !important;
        transition: all 0.3s ease !important;
        font-weight: 400 !important;
        line-height: 1.5 !important;
    }
    
    .age-restricted-link:hover {
        color: #00d97a !important;
        text-decoration: underline !important;
    }
    
    /* Remove any extra spacing */
    .stTextInput > div {
        margin-bottom: 0 !important;
    }
    
    .stLinkButton {
        margin-top: 0 !important;
    }
    
    /* FAQ hover effect */
    .faq-card {
        background-color: #2d2d2d !important;
        border-radius: 12px !important;
        padding: 2rem !important;
        margin-bottom: 1.5rem !important;
        border: 1px solid #3a3a3a !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease !important;
    }
    
    .faq-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 20px rgba(0, 217, 122, 0.15);
    }
    
    /* Ensure FAQ section is visible */
    .faq-container {
        max-width: 800px;
        margin: 4rem auto 2rem auto;
        padding: 0 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Centered title with icon - exactly like original
st.markdown("""
<div class="main-title">
    <span class="link-icon">🔗</span>
    치지직 VOD 다운로더
</div>
""", unsafe_allow_html=True)

# Input section - clean layout like original
st.markdown('<div class="input-section">', unsafe_allow_html=True)

# URL input field
url_input = st.text_input(
    "VOD URL", 
    placeholder="chzzk.naver.com/video/{number}",
    key="vod_url"
)

# Build URL for redirect
if url_input.strip():
    clean_url = url_input.strip()
    if not clean_url.startswith('http'):
        formatted_url = f"https://{clean_url}"
    else:
        formatted_url = clean_url
    download_url = f"https://chzzkdownloader.com?utm_source=streamlit&url={formatted_url}"
else:
    download_url = "https://chzzkdownloader.com?utm_source=streamlit"

# Button - original style
st.link_button(
    "VOD 가져오기",
    download_url
)

# Age-restricted download link
st.markdown("""
<div style="text-align: center; margin-top: 16px;">
    <a href="https://www.paypal.com/ncp/payment/LM7VS22YPJVKJ" target="_blank" class="age-restricted-link">
        연령 제한 콘텐츠 다운로드가 필요하신가요? 프로 버전을 구매하세요!
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Add some spacing
st.markdown("<br><br>", unsafe_allow_html=True)

# FAQ Section Title
st.markdown("""
<h2 style="color: #00d97a; font-size: 1.8rem; text-align: center; margin: 2rem 0; font-weight: 600;">
    자주 묻는 질문 (FAQ)
</h2>
""", unsafe_allow_html=True)

# FAQ Container
st.markdown('<div class="faq-container">', unsafe_allow_html=True)

# FAQ items using expander (native Streamlit component for better compatibility)
with st.expander("🎬 치지직 클립 다운로드는 어떻게 하나요?", expanded=False):
    st.markdown("""
    <p style="color: #cccccc; line-height: 1.6;">
        <a href="https://chzzkdownloader.com?utm_source=faq" style="color: #00d97a; text-decoration: none; font-weight: 500;">chzzkdownloader.com</a>에서 
        치지직 클립 URL을 붙여넣기만 하면 됩니다. 클릭 몇 번으로 고품질 클립을 저장할 수 있습니다.
    </p>
    """, unsafe_allow_html=True)

with st.expander("📱 치지직 모바일 다운로드도 가능한가요?", expanded=False):
    st.markdown("""
    <p style="color: #cccccc; line-height: 1.6;">
        네! <a href="https://chzzkdownloader.com?utm_source=faq" style="color: #00d97a; text-decoration: none; font-weight: 500;">chzzkdownloader.com</a>은 
        모바일에서도 완벽하게 작동합니다. 스마트폰에서 치지직 다시보기와 클립을 쉽게 다운로드하세요.
    </p>
    """, unsafe_allow_html=True)

with st.expander("🎵 치지직 영상을 음원(오디오)으로 변환할 수 있나요?", expanded=False):
    st.markdown("""
    <p style="color: #cccccc; line-height: 1.6;">
        물론입니다! <a href="https://chzzkdownloader.com?utm_source=faq" style="color: #00d97a; text-decoration: none; font-weight: 500;">chzzkdownloader.com</a>은 
        오디오 변환 기능을 제공합니다. 치지직 VOD에서 음악이나 대화만 추출하여 MP3로 저장할 수 있습니다.
    </p>
    """, unsafe_allow_html=True)

with st.expander("💎 치지직 VOD 다운로더로 무엇을 다운로드할 수 있나요?", expanded=False):
    st.markdown("""
    <p style="color: #cccccc; line-height: 1.6;">
        <a href="https://chzzkdownloader.com?utm_source=faq" style="color: #00d97a; text-decoration: none; font-weight: 500;">chzzkdownloader.com</a>을 사용하면 
        치지직의 모든 공개 VOD, 다시보기 영상, 클립을 고품질로 다운로드할 수 있습니다. 가장 빠르고 안정적인 치지직 다운로더입니다.
    </p>
    """, unsafe_allow_html=True)

with st.expander("⚡ 왜 chzzkdownloader.com을 사용해야 하나요?", expanded=False):
    st.markdown("""
    <div style="color: #cccccc; line-height: 1.6;">
        ✅ 무료 사용 가능<br>
        ✅ 빠른 다운로드 속도<br>
        ✅ 고품질 영상 지원<br>
        ✅ 오디오 변환 기능<br>
        ✅ 모바일 완벽 지원<br>
        ✅ 설치 불필요 - 웹에서 바로 사용
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# CTA Button
st.markdown("""
<div style="text-align: center; margin: 3rem 0 2rem 0;">
    <a href="https://chzzkdownloader.com?utm_source=faq_cta" 
       style="display: inline-block; background: linear-gradient(135deg, #00d97a, #00b368); 
              color: white; padding: 14px 32px; border-radius: 8px; text-decoration: none; 
              font-weight: 600; font-size: 16px; box-shadow: 0 4px 15px rgba(0, 217, 122, 0.3); 
              transition: transform 0.2s;">
        🚀 지금 바로 다운로드 시작하기
    </a>
</div>
""", unsafe_allow_html=True)

# SEO-friendly text content for search engines
st.markdown("""
<div style="display: none;">
치지직 VOD 다운로더는 CHZZK(치지직) 플랫폼의 비디오 온 디맨드(VOD) 콘텐츠를 쉽고 빠르게 다운로드할 수 있는 무료 온라인 도구입니다. 
네이버의 게임 스트리밍 플랫폼인 치지직에서 제공되는 다양한 VOD 영상을 고품질로 저장할 수 있으며, 
별도의 소프트웨어 설치 없이 웹브라우저에서 바로 이용 가능합니다. 
안전하고 신뢰할 수 있는 다운로드 서비스로 개인정보 보호를 최우선으로 합니다.
치지직 클립 다운로드, 치지직 다시보기 다운로드, 치지직 영상 다운로드, 치지직 오디오 변환 모두 가능합니다.
</div>
""", unsafe_allow_html=True)

# Structured data for SEO
st.markdown("""
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "치지직 VOD 다운로더",
  "description": "CHZZK 비디오를 빠르고 안전하게 다운로드하는 무료 온라인 도구",
  "url": "https://chzzkdownloader.com",
  "applicationCategory": "Multimedia",
  "operatingSystem": "Any",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "KRW"
  }
}
</script>
""", unsafe_allow_html=True)

# Add padding at bottom to ensure scrollability
st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
