#=== Delete files from homeassistant service ===#
#=== exlab, Jan. 02, 2019 ===#
#==================#
# Code for Home Assistant
# Code in configuration.yaml
# hass_delete:
# Code in automation
# - alias: Example delete files
  # trigger:
    # platform: state
    # entity_id: domain.entity_id
    # to: 'on'
  # action:
    # service: hass_delete.files
    # data:
      # file_path: '/config/folder/file_name1.extension, /config/folder/file_name2.extension'
#==================#	  

domain = 'hass_delete'
import os

def setup(homeassistant, config):
  def delete_file(files):
    # Declare variable in Home Assistant: file_path
    file_path = files.data.get('file_path')
    #if list files by delimiter ","
    sDelimiter = ','
    file_path = file_path.replace(', ', sDelimiter)
    if file_path.find(sDelimiter) > 0:
      array_paths = file_path.split(sDelimiter)
      for iTem in array_paths:
        if os.path.exists(iTem):
          os.remove(iTem)
    else:
      if os.path.exists(file_path):
        os.remove(file_path)
  homeassistant.services.register(domain, 'files', delete_file)
  return True
