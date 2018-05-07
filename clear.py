def cleanup():
	import os, shutil, config

	for the_file in os.listdir(config.upload_folder):
		file_path = os.path.join(config.upload_folder, the_file)
		try:
			if os.path.isfile(file_path):
				os.unlink(file_path)
		except Exception as e:
			print(e)
	return "Cleared out creative folders"