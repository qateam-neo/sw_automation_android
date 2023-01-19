
import sys
import os
import platform
class Pythonpath():
    def check_if_folders_available(self):
        Files=os.listdir(self.path)
        available_folders=[]
        folder_available=False
        for File in Files:
            # print(File)
            if os.path.isdir(self.path+"/"+File) and File[0]!="." and not "pycache" in File:  
                folder_available=True
                available_folders.append(File)
        if folder_available == False:
            return False
        else:
            return available_folders
            
    def _navigate_path_to_main(self):
        self.path= os.getcwd() 
        while  not self.path.endswith("sw_automation_android"):
            self.path= self.path[:-1]

    def _remove_last_folder_from_path(self,Folder):
        # print(self.path)
        while self.path.endswith("/")==False:
            self.path= self.path[:-1]
            # print(self.path)
        self.path= self.path[:-1]
        # print(self.path)

        
    def check_platform(self):
            
        self.Platform=platform.platform()

        if "macos" in  self.Platform.lower():
            self.Platform= "mac"
        elif "windows" in self.Platform.lower():
            self.Platform="windows"

    def _add_paths_from_folder(self):
        Files=os.listdir(self.path)
        # print("Adding Files to path inside "+self.path)
        # print(Files)
        
        for File in Files:
            folder_available=False
            if os.path.isdir(self.path+"/"+File) and File[0]!="." and not "pycache" in File:  
                folder_available=True
                sys.path.append(self.path+"/"+File)
                # print("This File was Added to path "+File)



    def AddAllPaths(self):
        self.System_Path=sys.path
        self.check_platform()
        self._navigate_path_to_main()
        
        if self.Platform == "mac":  
            self.path= os.getcwd() 
            Files=os.listdir(self.path)
            
            # print(Files)
            for File in Files:
                # print(os.path.isdir(File))
                if "." not in File:  
                    sys.path.append(self.path+"/"+File)
                    # print(self.path+"/"+File)


        if self.Platform == "windows":  
            
            folder_available=False
            self._navigate_path_to_main()
            print(self.path)
            available_folders=self.check_if_folders_available()
            # print(self.path)
            if available_folders!=False:    
                self._add_paths_from_folder()
                # print(self.path)
            else:print("Change path")
            
            
            for File in available_folders:
                self.path=self.path+"/"+File
                # print(self.path)
                available_folders=self.check_if_folders_available()
                # print(available_folders)
                if available_folders!=False:
                    self._add_paths_from_folder()
                    for mini_file in available_folders:
                        # print("\t"+mini_file)
                        self.path=self.path+"/"+mini_file
                        # print(self.path)
                        available_folders=self.check_if_folders_available()
                        if available_folders!=False:   
                            self._add_paths_from_folder()
                            for mini_mini_file in available_folders:
                                # print("\t"+mini_mini_file)
                                self.path=self.path+"/"+mini_mini_file
                                # print(self.path)
                                available_folders=self.check_if_folders_available()
                                if available_folders!=False:   
                                    self._add_paths_from_folder()
                                    # print(self.path)
                                    for mini_mini_mini_file in available_folders:
                                        self.path=self.path+"/"+mini_mini_mini_file
                                        # print(self.path)
                                        available_folders=self.check_if_folders_available()
                                        if available_folders!=False:   
                                            self._add_paths_from_folder()
                                        else:
                                            self._remove_last_folder_from_path(mini_mini_mini_file)
                                            # print(self.path)
                                    self._remove_last_folder_from_path(mini_mini_file)
                                else:
                                    self._remove_last_folder_from_path(mini_mini_file)
                            self._remove_last_folder_from_path(mini_mini_file)
                        else:
                            self._remove_last_folder_from_path(mini_file)
                else:
                    self._remove_last_folder_from_path(File)
                self._navigate_path_to_main()
                # print(self.path)
                
            # print("")
            # print("")




a=Pythonpath().AddAllPaths()
print(sys.path)