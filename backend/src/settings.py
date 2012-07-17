# This is an example settings file. Customize these values for your
# app and rename the file as settings.py.

settings = {
    # put your AWS account access key and secret here
	"aws_access_key_id": "",
	"aws_secret_access_key": "",
	
	"service_name":"AWSMechanicalTurkRequester",
	"service_version":"2007-03-12",
	"service_url":"https://mechanicalturk.sandbox.amazonaws.com",
	"external_submit":"https://workersandbox.mturk.com/mturk/externalSubmit",


	"tensentencesHITtype":{
		"AssignmentDurationInSeconds":"3600", # 1 hour - 3600 seconds
		"Description":"Translate 10 tweets from Spanish to English",
		'Reward.1.Amount':'0.15',
		'Reward.1.CurrencyCode':'USD',
		"Title":"Translate 10 tweets from Spanish to English",
		"AutoApprovalDelayInSeconds":"604800", #  7 days - 604 800 seconds
		"Keywords":"translation, tweets, dictionary, foreign, English, language, research, JHU",
		#"QualificationRequirement.1.QualificationTypeId":"00000000000000000040", # Worker_NumberHITsApproved
		#"QualificationRequirement.1.Comparator":"GreaterThan",
		#"QualificationRequirement.1.IntegerValue":"50",
		"QualificationRequirement.1.QualificationTypeId":"000000000000000000L0", # Worker_PercentAssignmentsApproved
		"QualificationRequirement.1.Comparator":"GreaterThan",
		"QualificationRequirement.1.IntegerValue":"85",
		
	},


	"similarHITtype":{
		"AssignmentDurationInSeconds":"3600", # 1 hour - 3600 seconds
		"Description":"Do these tweets have the same meaning?",
		'Reward.1.Amount':'0.10',
		'Reward.1.CurrencyCode':'USD',
		"Title":"Do these tweets have the same meaning?",
		"AutoApprovalDelayInSeconds":"604800", #  7 days - 604 800 seconds
		"Keywords":"similar, tweets, dictionary, English, language, research, JHU",
		#"QualificationRequirement.1.QualificationTypeId":"00000000000000000040", # Worker_NumberHITsApproved
		#"QualificationRequirement.1.Comparator":"GreaterThan",
		#"QualificationRequirement.1.IntegerValue":"50",
		"QualificationRequirement.1.QualificationTypeId":"000000000000000000L0", # Worker_PercentAssignmentsApproved
		"QualificationRequirement.1.Comparator":"GreaterThan",
		"QualificationRequirement.1.IntegerValue":"85",
	
	},

    "dbname":"tweets_es",
    "user":"dkachaev",
    "host":"localhost",


	"languages_file":"../data/languages.txt",
	#"languages_file":"data/languages/sample_languages.txt",
    "target_language":"en",
    "target_language_name":"English",

	"max_assignments":3, #max assignments per HIT in MTurk
	"lifetimeinseconds":5184000, #lifetime of task in MTurk in seconds (5 184 000 seconds - 60 day)
	"web_enpoint_domain":"mturk.jhu.edu",
	"web_endpoint_tensentences_hit_path":"/hits/tensentences",

	"web_endpoint_similar_hit_path":"/hits/similar",

	"mturk_autoapproval_treshold":10, # first 10 assignments for each HITType are autoapproved


	"num_context_sentences":3,
	"num_knowns":2,	# control words
	"num_unknowns":8, # unknown words to translate (10 (twelve total words to translate in HIT))

	"similar_num_unknowns":4, # number of items in synonyms task
	"similar_num_knowns":1, # number of items in synonyms task (control)
	
	"similar_approve_feedback":"Thank you!",
	"similar_reject_feedback":"Sorry, your results didn't pass our quality control.",

	"tensentences_approve_feedback":"Thank you!",
	"tensentences_reject_feedback":"Sorry, your results didn't pass our quality control.",

	
	"number_of_similar":10, #number of synonyms used as control
	
	"run_name":"test", # name of this particular config/run (used as prefix for generated output files)
	
	
}




