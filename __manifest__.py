{
    'name':'Interior Design',

    'depends':['base','website','portal','website_sale','crm','sale',],
    'data':['views/design_views.xml',
            'views/add_new_fields_crm_lead_views.xml',
            'views/designs_studio_views.xml',
          
        ],
    'assets': {
        'web.assets_frontend': [
            'interior/static/src/css/design_style.css',
            'interior/static/src/js/design.js',
            
            

        ],
       
    },
   
}