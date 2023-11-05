from django.urls import path,include
from Farmer import views
app_name="webfarmer"
urlpatterns = [
    path('home/',views.home,name="home"),
    path('My_profile/',views.my_pro,name="my_pro"), 
    path('editprofile/',views.editprofile,name="editprofile"),
    path('editpropic/',views.editpropic,name="editpropic"),
    path('changepass/',views.changepass,name="changepass"),
    path('search_market/',views.search_mar,name="search_mar"),
    path('marketprofile/<int:mproid>',views.marketprofile,name="marketprofile"),
    path('ajaxmarket/',views.ajaxmarket,name="ajaxmarket"),
    path('marketproduct/<int:marid>',views.marketproduct,name="marketproduct"),
    path('ajaxmarketproduct/',views.ajaxmarketproduct,name="ajaxmarketproduct"),
    path('marketcart/<int:marketpdtid>',views.marketcart,name="marketcart"),
    path('mycart/',views.mycart,name="mycart"),
    path('ajaxmarketpdtamt/',views.ajaxmarketpdtamt,name="ajaxmarketpdtamt"),
    path('mdeletecartitem/<int:mcartid>',views.mdeletecartitem,name="mdeletecartitem"),
    path('mpayment/<int:mamt>',views.mpayment,name="mpayment"),
    path('mpaymentoffline/<int:am>',views.mpaymentoffline,name="mpaymentoffline"),
    path('product/',views.product,name="product"),
    path('ajaxsubcat/',views.ajaxsubcat,name="ajaxsubcat"),
    path('stock/<int:stid>',views.stock,name="stock"),
    path('deleteitem/<int:delit>',views.deleteitem,name="deleteitem"),
    path('complaint/',views.complaint,name="complaint"),
    path('feedback/',views.feedback,name="feedback"),  
    path('loader/',views.loader,name="loader"),
    path('paymentsuc/',views.paymentsuc,name="paymentsuc"),  
    path('mdeletecartitem/<int:mcartid>',views.mdeletecartitem,name="mdeletecartitem"), 
    path('reply/',views.reply,name="reply"),
    path('myproduct/<int:bkid>',views.myproduct,name="myproduct"),
    path('deleteitemcart/<int:delid>',views.deleteitemcart,name="deleteitemcart"),
    path('mybookings/',views.mybookings,name="mybookings"),
    path('bills/<int:bookid>',views.bills,name="bills"),
    path('viewevents/<int:eventid>',views.viewevents,name="viewevents"),
    path('applyevents/<int:apid>',views.applyevents,name="applyevents"),
    path('apllied/',views.applied,name="apply"),
    path('viewapplicationrequuest/',views.viewapplicationrequuest,name="viewapplicationrequuest"),
    path('buyers/',views.buyers,name="buyers"),
    path('buyerspdt/<int:bookid>',views.buyerspdt,name="buyerspdt"),
    path('delivery/<int:cartid>',views.delivery,name="delivery"),
    path('delivereditem/',views.delivereditem,name="delivereditem"),
    path('deleteeventapply/<int:delev>',views.deleteeventapply,name="deleteeventapply"),
    path('report/',views.report,name="report"),
    path('logout/',views.logout,name="logout"),
    path('ajaxfreport/',views.ajaxfreport,name="ajaxfreport"),
    path('buyreport/',views.buyreport,name="buyreport"),
    path('ajaxbuyreport/',views.ajaxbuyreport,name="ajaxbuyreport"),
    path('mydeliveredproduct/<int:productid>',views.mydeliveredproduct,name="mydeliveredproduct"),
    path('deliveredbills/<int:billid>',views.deliveredbills,name="deliveredbills"),
    path('customerdelivereditem/<int:custid>',views.customerdelivereditem,name="customerdelivereditem"),
] 