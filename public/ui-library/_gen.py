import re

dash=open("executive_dashboard.html").read()
head=dash[:dash.index("</head>")+len("</head>")]

NAV=[
 ("dashboard","/ui-library/executive_dashboard.html","dashboard","Dashboard",""),
 ("transactions","/ui-library/transaction_ledger.html","receipt_long","Transactions",""),
 ("invoices","/ui-library/invoices_ebm_receipts.html","description","Invoices",""),
 ("tax","/ui-library/tax_compliance_center.html","gavel","Tax & Compliance",""),
 ("banking","/ui-library/banking.html","account_balance","Banking",""),
 ("reports","/ui-library/reports.html","assessment","Reports",""),
 ("ai_advisor","/ui-library/ai_advisor.html","psychology","AI Advisor",
   '<span class="ml-auto flex h-2 w-2 rounded-full bg-secondary-fixed-dim animate-pulse"></span>'),
 ("settings","/ui-library/settings.html","settings","Settings",""),
]

def nav_html(active):
    out=[]
    for key,href,icon,label,extra in NAV:
        if key==active:
            cls='flex items-center gap-3 px-4 py-3 bg-white/10 text-secondary-fixed-dim border-l-4 border-secondary-fixed-dim transition-all opacity-90'
        else:
            cls='flex items-center gap-3 px-4 py-3 text-on-primary-container/70 hover:bg-white/5 hover:text-white transition-colors'
        out.append(f'<a class="{cls}" href="{href}">')
        out.append(f'<span class="material-symbols-outlined" data-icon="{icon}">{icon}</span>')
        out.append(f'<span class="font-body-md">{label}</span>')
        if extra: out.append(extra)
        out.append('</a>')
    return "\n".join(out)

def sidebar(active):
    return f'''<aside id="app-sidebar" class="-translate-x-full md:translate-x-0 transition-transform duration-300 w-sidebar-width h-screen fixed left-0 top-0 bg-primary-container text-on-primary-container flex flex-col py-container-margin border-r border-outline-variant z-50">
<div class="px-6 mb-10 flex items-center gap-3">
<div class="w-10 h-10 bg-secondary-fixed-dim rounded-lg flex items-center justify-center">
<span class="material-symbols-outlined text-primary-container" style="font-variation-settings: 'FILL' 1;">account_balance</span>
</div>
<div>
<h1 class="text-headline-lg font-bold text-white tracking-tight">FinAgent</h1>
<p class="text-[10px] uppercase tracking-widest text-on-primary-container/60 font-bold">Rwanda SME Edition</p>
</div>
</div>
<nav class="flex-grow space-y-1">
{nav_html(active)}
</nav>
<div class="mt-auto px-4 border-t border-white/10 pt-6">
<div class="bg-white/5 rounded-xl p-4 mb-4">
<div class="flex items-center gap-2 mb-1">
<span class="material-symbols-outlined text-secondary-fixed-dim text-sm" data-icon="bolt">bolt</span>
<span class="text-[11px] font-bold text-white uppercase tracking-wider">AI Agent: Active</span>
</div>
<p class="text-[12px] text-on-primary-container/60">Monitoring tax deadlines &amp; liquidity.</p>
</div>
<a class="flex items-center gap-3 px-4 py-3 text-on-primary-container/70 hover:bg-white/5 hover:text-white transition-colors" href="#">
<span class="material-symbols-outlined" data-icon="help">help</span>
<span class="font-body-md">Help Center</span>
</a>
</div>
</aside>'''

def header(title):
    return f'''<header class="h-16 flex justify-between items-center px-container-margin max-md:pl-16 sticky top-0 bg-surface border-b border-outline-variant z-40">
<div class="flex items-center gap-6">
<h2 class="font-headline-md text-headline-md font-bold text-primary">FinAgent Rwanda</h2>
<div class="relative w-80 hidden md:block">
<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-outline" data-icon="search">search</span>
<input class="w-full bg-surface-container-low border-none rounded-lg pl-10 pr-4 py-2 text-body-sm focus:ring-2 focus:ring-primary/20" placeholder="Search {title.lower()}..." type="text"/>
</div>
</div>
<div class="flex items-center gap-4">
<button class="p-2 text-on-surface-variant hover:bg-surface-container-high transition-colors rounded-full relative">
<span class="material-symbols-outlined" data-icon="notifications">notifications</span>
<span class="absolute top-2 right-2 w-2 h-2 bg-error rounded-full"></span>
</button>
<button class="p-2 text-on-surface-variant hover:bg-surface-container-high transition-colors rounded-full">
<span class="material-symbols-outlined" data-icon="translate">translate</span>
</button>
<div class="h-8 w-[1px] bg-outline-variant mx-2"></div>
<div class="flex items-center gap-3">
<div class="text-right">
<p class="text-body-sm font-bold text-on-surface">Kigali Tech Ltd</p>
<p class="text-[10px] text-on-surface-variant">Admin Access</p>
</div>
<div class="w-10 h-10 rounded-full border-2 border-primary-fixed-dim bg-primary-container flex items-center justify-center text-white font-bold shadow-sm">KT</div>
</div>
</div>
</header>'''

FOOTER='''<button id="navToggle" aria-label="Toggle navigation" class="md:hidden fixed top-3 left-3 z-[70] w-10 h-10 flex items-center justify-center rounded-lg bg-primary-container text-white shadow-lg">
<span id="navToggleIcon" class="material-symbols-outlined">menu</span>
</button>
<div id="navOverlay" class="md:hidden fixed inset-0 bg-black/40 z-[45] hidden"></div>
<script>
(function(){
  var side=document.getElementById('app-sidebar');
  var btn=document.getElementById('navToggle');
  var ov=document.getElementById('navOverlay');
  var icon=document.getElementById('navToggleIcon');
  if(!side||!btn||!ov)return;
  function isOpen(){return !side.classList.contains('-translate-x-full');}
  function open(){side.classList.remove('-translate-x-full');ov.classList.remove('hidden');if(icon)icon.textContent='close';document.body.style.overflow='hidden';}
  function close(){side.classList.add('-translate-x-full');ov.classList.add('hidden');if(icon)icon.textContent='menu';document.body.style.overflow='';}
  btn.addEventListener('click',function(e){e.stopPropagation();isOpen()?close():open();});
  ov.addEventListener('click',close);
  document.addEventListener('click',function(e){if(window.innerWidth<768&&isOpen()&&!side.contains(e.target)&&!btn.contains(e.target))close();});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});
  side.querySelectorAll('a[href]').forEach(function(a){a.addEventListener('click',function(){if(window.innerWidth<768)close();});});
  window.addEventListener('resize',function(){if(window.innerWidth>=768)close();});
})();
</script>'''

def page(active,title,subtitle,body,titletag):
    h=head.replace("<title>FinAgent Rwanda | Executive Dashboard</title>",f"<title>FinAgent Rwanda | {titletag}</title>")
    return f'''{h}
<body style="overflow-x:hidden" class="bg-background text-on-background font-body-md overflow-x-hidden">
{sidebar(active)}
<main class="md:ml-sidebar-width min-h-screen flex flex-col">
{header(title)}
<div class="p-container-margin flex flex-col gap-gutter max-w-[1600px] mx-auto w-full">
<div class="flex justify-between items-end mb-2">
<div>
<h3 class="font-headline-xl text-headline-xl text-primary tracking-tight">{title}</h3>
<p class="text-on-surface-variant">{subtitle}</p>
</div>
</div>
{body}
</div>
</main>
{FOOTER}
</body></html>'''

def stat(icon,label,value,sub,color="secondary"):
    return f'''<div class="bg-surface-container-lowest rounded-xl p-5 border border-outline-variant flex flex-col gap-3">
<div class="flex items-center justify-between">
<div class="w-10 h-10 rounded-lg bg-{color}-container flex items-center justify-center">
<span class="material-symbols-outlined text-primary-container" data-icon="{icon}">{icon}</span>
</div>
<span class="text-label-caps text-on-surface-variant uppercase">{label}</span>
</div>
<p class="text-headline-lg font-bold text-on-surface font-data-rwf">{value}</p>
<p class="text-body-sm text-on-surface-variant">{sub}</p>
</div>'''

def card(title,inner,action=""):
    return f'''<div class="bg-surface-container-lowest rounded-xl border border-outline-variant overflow-hidden">
<div class="flex items-center justify-between px-5 py-4 border-b border-outline-variant">
<h4 class="font-headline-md text-headline-md text-on-surface">{title}</h4>
{action}
</div>
<div class="p-5">{inner}</div>
</div>'''

# ---- BANKING ----
bank_accounts=""
for name,bank,num,bal,badge in [
  ("Operating Account","Bank of Kigali","****4021","RWF 12,480,000","Primary"),
  ("Payroll Account","I&M Bank","****8834","RWF 3,150,000","Payroll"),
  ("Tax Reserve","Bank of Kigali","****2290","RWF 5,720,000","Reserve"),
  ("USD Account","Equity Bank","****1177","USD 18,400","FX"),
]:
    bank_accounts+=f'''<div class="flex items-center justify-between p-4 rounded-lg border border-outline-variant hover:bg-surface-container-low transition-colors">
<div class="flex items-center gap-4">
<div class="w-11 h-11 rounded-lg bg-primary-container flex items-center justify-center text-white">
<span class="material-symbols-outlined" data-icon="account_balance">account_balance</span>
</div>
<div>
<p class="font-bold text-on-surface">{name}</p>
<p class="text-body-sm text-on-surface-variant">{bank} &bull; {num}</p>
</div>
</div>
<div class="text-right">
<p class="font-data-rwf font-bold text-on-surface">{bal}</p>
<span class="text-[10px] font-bold uppercase bg-secondary-container text-on-secondary-container px-2 py-1 rounded">{badge}</span>
</div>
</div>'''

bank_tx=""
for d,desc,acc,amt,pos in [
  ("Jul 05","MTN MoMo Payout","Operating","+RWF 840,000",True),
  ("Jul 04","Airtel Bulk Payment","Payroll","-RWF 1,200,000",False),
  ("Jul 03","Client Wire - Andela","USD Account","+USD 4,500",True),
  ("Jul 02","RRA Tax Transfer","Tax Reserve","-RWF 620,000",False),
  ("Jul 01","Supplier - Simba Supermarket","Operating","-RWF 310,000",False),
]:
    color="text-secondary" if pos else "text-error"
    bank_tx+=f'''<tr class="zebra-stripe border-b border-outline-variant">
<td class="py-3 px-2 text-body-sm text-on-surface-variant">{d}</td>
<td class="py-3 px-2 text-body-sm font-medium text-on-surface">{desc}</td>
<td class="py-3 px-2 text-body-sm text-on-surface-variant">{acc}</td>
<td class="py-3 px-2 text-right font-data-rwf {color} font-medium">{amt}</td>
</tr>'''

banking_body=f'''<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-gutter mb-2">
{stat("account_balance_wallet","Total Balance","RWF 21.3M","Across 4 accounts")}
{stat("trending_up","Inflows (MTD)","RWF 8.4M","+12% vs last month","tertiary")}
{stat("trending_down","Outflows (MTD)","RWF 5.1M","-4% vs last month","error")}
{stat("sync","Last Sync","2 min ago","BK & I&M connected")}
</div>
<div class="grid grid-cols-1 lg:grid-cols-3 gap-gutter">
<div class="lg:col-span-2">{card("Linked Accounts", '<div class="flex flex-col gap-3">'+bank_accounts+'</div>', '<button class="flex items-center gap-1 text-body-sm font-bold text-primary"><span class="material-symbols-outlined text-[18px]" data-icon="add">add</span>Link account</button>')}</div>
<div>{card("Cash Position", '''<div class="flex flex-col items-center justify-center py-6">
<div class="relative w-40 h-40 rounded-full flex items-center justify-center" style="background:conic-gradient(#046b5e 0 62%,#ffb787 62% 85%,#ba1a1a 85% 100%)">
<div class="w-28 h-28 rounded-full bg-surface-container-lowest flex flex-col items-center justify-center">
<span class="text-[11px] uppercase text-on-surface-variant">Healthy</span>
<span class="font-data-rwf font-bold text-on-surface">62%</span>
</div>
</div>
<div class="mt-6 w-full space-y-2 text-body-sm">
<div class="flex justify-between"><span class="flex items-center gap-2"><span class="w-3 h-3 rounded-full bg-secondary"></span>Operating</span><span class="font-data-rwf">62%</span></div>
<div class="flex justify-between"><span class="flex items-center gap-2"><span class="w-3 h-3 rounded-full bg-tertiary-fixed-dim"></span>Reserves</span><span class="font-data-rwf">23%</span></div>
<div class="flex justify-between"><span class="flex items-center gap-2"><span class="w-3 h-3 rounded-full bg-error"></span>Committed</span><span class="font-data-rwf">15%</span></div>
</div>
</div>''')}</div>
</div>
{card("Recent Bank Transactions", f'<div class="overflow-x-auto"><table class="w-full"><thead><tr class="text-label-caps uppercase text-on-surface-variant border-b border-outline-variant"><th class="text-left py-2 px-2">Date</th><th class="text-left py-2 px-2">Description</th><th class="text-left py-2 px-2">Account</th><th class="text-right py-2 px-2">Amount</th></tr></thead><tbody>{bank_tx}</tbody></table></div>')}'''

open("banking.html","w").write(page("banking","Banking","Manage connected accounts, balances and cash flow",banking_body,"Banking"))

# ---- REPORTS ----
report_cards=""
for icon,name,desc,tag in [
  ("summarize","Profit & Loss","Revenue, expenses and net margin","Monthly"),
  ("account_balance","Balance Sheet","Assets, liabilities and equity","Quarterly"),
  ("payments","Cash Flow Statement","Operating, investing & financing","Monthly"),
  ("receipt_long","VAT Return Summary","Output & input VAT for RRA","Monthly"),
  ("groups","Payroll Report","PAYE, RSSB and net pay","Monthly"),
  ("insights","Expense Breakdown","Spend by category & vendor","Custom"),
]:
    report_cards+=f'''<div class="bg-surface-container-lowest rounded-xl p-5 border border-outline-variant flex flex-col gap-3 hover:shadow-md transition-shadow">
<div class="flex items-center justify-between">
<div class="w-11 h-11 rounded-lg bg-primary-container flex items-center justify-center text-white"><span class="material-symbols-outlined" data-icon="{icon}">{icon}</span></div>
<span class="text-[10px] font-bold uppercase bg-surface-container-high text-on-surface-variant px-2 py-1 rounded">{tag}</span>
</div>
<p class="font-bold text-on-surface">{name}</p>
<p class="text-body-sm text-on-surface-variant flex-grow">{desc}</p>
<div class="flex gap-2 pt-2">
<button class="flex-1 flex items-center justify-center gap-1 text-body-sm font-bold text-primary border border-outline-variant rounded-lg py-2 hover:bg-surface-container-low"><span class="material-symbols-outlined text-[16px]" data-icon="visibility">visibility</span>View</button>
<button class="flex items-center justify-center gap-1 text-body-sm font-bold text-white bg-primary-container rounded-lg px-3 py-2"><span class="material-symbols-outlined text-[16px]" data-icon="file_download">file_download</span></button>
</div>
</div>'''

bars=""
for m,h in [("Jan",55),("Feb",70),("Mar",48),("Apr",82),("May",64),("Jun",90),("Jul",76)]:
    bars+=f'<div class="flex flex-col items-center gap-2 flex-1"><div class="w-full bg-primary-container rounded-t" style="height:{h*1.6}px"></div><span class="text-[11px] text-on-surface-variant">{m}</span></div>'

reports_body=f'''<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-gutter mb-2">
{stat("payments","Total Revenue","RWF 48.2M","YTD 2024")}
{stat("shopping_cart","Total Expenses","RWF 31.6M","YTD 2024","error")}
{stat("savings","Net Profit","RWF 16.6M","34% margin","tertiary")}
{stat("description","Reports Generated","128","This year")}
</div>
{card("Revenue Trend (Monthly)", f'<div class="flex items-end gap-3 h-48 pt-4">{bars}</div>')}
<div class="mt-2">
<h4 class="font-headline-md text-headline-md text-on-surface mb-4">Standard Reports</h4>
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-gutter">{report_cards}</div>
</div>'''

open("reports.html","w").write(page("reports","Reports","Generate financial statements and business insights",reports_body,"Reports"))

# ---- AI ADVISOR ----
insights=""
for icon,title,text,tone in [
  ("warning","VAT deadline approaching","Your Q2 VAT return is due in 8 days. Estimated liability: RWF 620,000. I can prepare the filing draft now.","tertiary"),
  ("trending_up","Cash flow opportunity","Operating account has RWF 6.2M idle. Consider a 90-day fixed deposit at 11% to earn ~RWF 170,000.","secondary"),
  ("receipt_long","Duplicate expense detected","2 payments to 'Simba Supermarket' on Jul 01 look identical (RWF 310,000). Review to avoid double payment.","error"),
]:
    insights+=f'''<div class="ai-gradient-border pl-4 py-3">
<div class="flex items-start gap-3">
<span class="material-symbols-outlined text-{tone} mt-0.5" data-icon="{icon}">{icon}</span>
<div>
<p class="font-bold text-on-surface">{title}</p>
<p class="text-body-sm text-on-surface-variant mt-1">{text}</p>
<div class="flex gap-2 mt-3">
<button class="text-body-sm font-bold text-white bg-primary-container rounded-lg px-3 py-1.5">Take action</button>
<button class="text-body-sm font-bold text-primary px-3 py-1.5">Dismiss</button>
</div>
</div>
</div>
</div>'''

chat='''<div class="flex flex-col gap-4 h-[360px] overflow-y-auto pr-2">
<div class="flex gap-3">
<div class="w-8 h-8 rounded-full bg-primary-container flex items-center justify-center text-white shrink-0"><span class="material-symbols-outlined text-[18px]" data-icon="psychology">psychology</span></div>
<div class="bg-surface-container-low rounded-xl rounded-tl-none p-3 text-body-sm max-w-[80%]">Habari! I'm your FinAgent AI advisor. Ask me about cash flow, taxes, or business decisions.</div>
</div>
<div class="flex gap-3 justify-end">
<div class="bg-primary-container text-white rounded-xl rounded-tr-none p-3 text-body-sm max-w-[80%]">Can we afford to hire 2 new developers?</div>
</div>
<div class="flex gap-3">
<div class="w-8 h-8 rounded-full bg-primary-container flex items-center justify-center text-white shrink-0"><span class="material-symbols-outlined text-[18px]" data-icon="psychology">psychology</span></div>
<div class="bg-surface-container-low rounded-xl rounded-tl-none p-3 text-body-sm max-w-[80%]">Based on your RWF 21.3M balance and RWF 5.1M monthly burn, two mid-level developers (~RWF 2.4M/mo total) would extend runway to 5.8 months. I recommend hiring one now and the second after the Andela contract closes in September.</div>
</div>
</div>
<div class="mt-4 flex items-center gap-2 border-t border-outline-variant pt-4">
<input class="flex-1 bg-surface-container-low border-none rounded-lg px-4 py-3 text-body-sm focus:ring-2 focus:ring-primary/20" placeholder="Ask FinAgent anything..." type="text"/>
<button class="w-11 h-11 rounded-lg bg-primary-container text-white flex items-center justify-center"><span class="material-symbols-outlined" data-icon="send">send</span></button>
</div>'''

ai_body=f'''<div class="grid grid-cols-1 sm:grid-cols-3 gap-gutter mb-2">
{stat("auto_awesome","AI Confidence","98%","Data quality high")}
{stat("lightbulb","Active Insights","3","2 need action","tertiary")}
{stat("savings","Savings Identified","RWF 790K","This quarter","secondary")}
</div>
<div class="grid grid-cols-1 lg:grid-cols-2 gap-gutter">
<div>{card("Ask FinAgent", chat)}</div>
<div>{card("Proactive Insights", '<div class="flex flex-col gap-4">'+insights+'</div>')}</div>
</div>'''

open("ai_advisor.html","w").write(page("ai_advisor","AI Advisor","Smart recommendations and answers for your business",ai_body,"AI Advisor"))

# ---- SETTINGS ----
def toggle(on):
    pos="justify-end bg-secondary" if on else "justify-start bg-surface-container-high"
    return f'<span class="w-10 h-6 rounded-full flex items-center px-0.5 {pos}"><span class="w-5 h-5 rounded-full bg-white shadow"></span></span>'

def setting_row(icon,title,desc,control):
    return f'''<div class="flex items-center justify-between p-4 rounded-lg hover:bg-surface-container-low transition-colors">
<div class="flex items-center gap-4">
<span class="material-symbols-outlined text-on-surface-variant" data-icon="{icon}">{icon}</span>
<div><p class="font-medium text-on-surface">{title}</p><p class="text-body-sm text-on-surface-variant">{desc}</p></div>
</div>
{control}
</div>'''

profile='''<div class="flex items-center gap-4 mb-6">
<div class="w-16 h-16 rounded-full bg-primary-container flex items-center justify-center text-white text-headline-md font-bold">KT</div>
<div><p class="font-bold text-on-surface text-headline-md">Kigali Tech Ltd</p><p class="text-body-sm text-on-surface-variant">TIN: 102938475 &bull; Admin Access</p></div>
<button class="ml-auto text-body-sm font-bold text-primary border border-outline-variant rounded-lg px-4 py-2">Edit</button>
</div>
<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
<div><label class="text-label-caps uppercase text-on-surface-variant">Business Name</label><input class="w-full mt-1 bg-surface-container-low border-none rounded-lg px-3 py-2 text-body-sm" value="Kigali Tech Ltd"/></div>
<div><label class="text-label-caps uppercase text-on-surface-variant">Email</label><input class="w-full mt-1 bg-surface-container-low border-none rounded-lg px-3 py-2 text-body-sm" value="admin@kigalitech.rw"/></div>
<div><label class="text-label-caps uppercase text-on-surface-variant">Phone</label><input class="w-full mt-1 bg-surface-container-low border-none rounded-lg px-3 py-2 text-body-sm" value="+250 788 123 456"/></div>
<div><label class="text-label-caps uppercase text-on-surface-variant">Currency</label><select class="w-full mt-1 bg-surface-container-low border-none rounded-lg px-3 py-2 text-body-sm"><option>RWF - Rwandan Franc</option><option>USD - US Dollar</option></select></div>
</div>'''

prefs=setting_row("notifications","Push Notifications","Tax deadlines and cash alerts",toggle(True))+setting_row("mail","Email Reports","Weekly financial summary",toggle(True))+setting_row("dark_mode","Dark Mode","Reduce eye strain",toggle(False))+setting_row("psychology","AI Auto-Suggestions","Proactive advisor insights",toggle(True))

integrations=setting_row("account_balance","Bank of Kigali","Connected &bull; Last sync 2 min ago",'<span class="text-[10px] font-bold uppercase bg-secondary-container text-on-secondary-container px-2 py-1 rounded">Active</span>')+setting_row("account_balance","I&M Bank","Connected &bull; Last sync 5 min ago",'<span class="text-[10px] font-bold uppercase bg-secondary-container text-on-secondary-container px-2 py-1 rounded">Active</span>')+setting_row("smartphone","MTN MoMo","Connected for payments",'<span class="text-[10px] font-bold uppercase bg-secondary-container text-on-secondary-container px-2 py-1 rounded">Active</span>')+setting_row("gavel","RRA e-Tax","Link to auto-file returns",'<button class="text-body-sm font-bold text-primary border border-outline-variant rounded-lg px-3 py-1.5">Connect</button>')

security='<div class="flex flex-col">'+setting_row("password","Change Password","Last changed 3 months ago",'<button class="text-body-sm font-bold text-primary">Update</button>')+setting_row("verified_user","Two-Factor Auth","Extra login security",toggle(True))+setting_row("devices","Active Sessions","2 devices signed in",'<button class="text-body-sm font-bold text-primary">Manage</button>')+setting_row("logout","Sign Out","End your current session",'<button class="text-body-sm font-bold text-error">Sign out</button>')+'</div>'

settings_body=f'''<div class="grid grid-cols-1 lg:grid-cols-2 gap-gutter">
<div>{card("Business Profile", profile)}</div>
<div>{card("Preferences", '<div class="flex flex-col">'+prefs+'</div>')}</div>
<div>{card("Integrations", '<div class="flex flex-col">'+integrations+'</div>')}</div>
<div>{card("Security", security)}</div>
</div>'''

open("settings.html","w").write(page("settings","Settings","Manage your business profile, preferences and integrations",settings_body,"Settings"))

print("Generated 4 pages")
