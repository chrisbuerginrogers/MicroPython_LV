<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="16008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Palette" Type="Folder" URL="../Palette">
			<Property Name="NI.DISK" Type="Bool">true</Property>
		</Item>
		<Item Name="Processors" Type="Folder" URL="../Processors">
			<Property Name="NI.DISK" Type="Bool">true</Property>
		</Item>
		<Item Name="_AllThings uPython.vi" Type="VI" URL="../VIs/_AllThings uPython.vi"/>
		<Item Name="Bitbanging.vi" Type="VI" URL="../testing/Bitbanging.vi"/>
		<Item Name="Code.xctl" Type="XControl" URL="../VIs/ColorText/Code.xctl"/>
		<Item Name="dir.mnu" Type="Document" URL="../dir.mnu"/>
		<Item Name="ExecuteLineFromScript.vi" Type="VI" URL="../VIs/ExecuteLineFromScript.vi"/>
		<Item Name="HelpDialog.vi" Type="VI" URL="../VIs/HelpDialog.vi"/>
		<Item Name="OpenMVTestCode.vi" Type="VI" URL="../testing/OpenMVTestCode.vi"/>
		<Item Name="SaveForPrevious.vi" Type="VI" URL="../VIs/SaveForPrevious.vi"/>
		<Item Name="StripComments.vi" Type="VI" URL="../VIs/StripComments.vi"/>
		<Item Name="Systemlink Tag.xctl" Type="XControl" URL="../VIs/SystemLink/Systemlink Tag.xctl"/>
		<Item Name="test.vi" Type="VI" URL="../testing/test.vi"/>
		<Item Name="uPythonX.xctl" Type="XControl" URL="../VIs/uPythonX/uPythonX.xctl"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="user.lib" Type="Folder">
				<Item Name="BuildSyliineCommCluster.vi" Type="VI" URL="../VIs/SystemLink/BuildSyliineCommCluster.vi"/>
				<Item Name="BuildTree.vi" Type="VI" URL="../VIs/BuildTree.vi"/>
				<Item Name="CheckForEOL.vi" Type="VI" URL="../VIs/REPL/Subs/CheckForEOL.vi"/>
				<Item Name="CheckLoopLF.vi" Type="VI" URL="../VIs/REPL/Subs/CheckLoopLF.vi"/>
				<Item Name="ClearLineToPrompt.vi" Type="VI" URL="../VIs/REPL/Subs/ClearLineToPrompt.vi"/>
				<Item Name="DownloadRunMain.vi" Type="VI" URL="../VIs/DownloadRunMain.vi"/>
				<Item Name="FileNameDialog.vi" Type="VI" URL="../VIs/REPL/Subs/FileNameDialog.vi"/>
				<Item Name="GetFileListing.vi" Type="VI" URL="../VIs/REPL/Subs/GetFileListing.vi"/>
				<Item Name="GetTagName.vi" Type="VI" URL="../VIs/SystemLink/GetTagName.vi"/>
				<Item Name="GreenQuotes.vi" Type="VI" URL="../VIs/ColorText/GreenQuotes.vi"/>
				<Item Name="LoginCode.vi" Type="VI" URL="../VIs/SystemLink/LoginCode.vi"/>
				<Item Name="LoginDialogBox.vi" Type="VI" URL="../VIs/SystemLink/LoginDialogBox.vi"/>
				<Item Name="MP_StringToArray.vi" Type="VI" URL="../VIs/MP_StringToArray.vi"/>
				<Item Name="QueueMany.vi" Type="VI" URL="../VIs/REPL/Subs/QueueMany.vi"/>
				<Item Name="ReadFileContents.vi" Type="VI" URL="../VIs/REPL/Subs/ReadFileContents.vi"/>
				<Item Name="ReadWritePython.vi" Type="VI" URL="../VIs/ReadWritePython.vi"/>
				<Item Name="ReadWriteREPL.vi" Type="VI" URL="../VIs/ReadWriteREPL.vi"/>
				<Item Name="RemoveBackspace.vi" Type="VI" URL="../VIs/RemoveBackspace.vi"/>
				<Item Name="REPL_Comm.vi" Type="VI" URL="../VIs/REPL/REPL_Comm.vi"/>
				<Item Name="ReplaceCodes.vi" Type="VI" URL="../VIs/REPL/Subs/ReplaceCodes.vi"/>
				<Item Name="RWSkylinePrefCluster.vi" Type="VI" URL="../VIs/SystemLink/RWSkylinePrefCluster.vi"/>
				<Item Name="SaveOnMP.vi" Type="VI" URL="../VIs/REPL/Subs/SaveOnMP.vi"/>
				<Item Name="SavePyFile.vi" Type="VI" URL="../VIs/SavePyFile.vi"/>
				<Item Name="SendScriptToQueue.vi" Type="VI" URL="../VIs/REPL/Subs/SendScriptToQueue.vi"/>
				<Item Name="Skyline_ReadWritePoly.vi" Type="VI" URL="../VIs/SystemLink/Skyline_ReadWritePoly.vi"/>
				<Item Name="SkylineCluster.ctl" Type="VI" URL="../VIs/SystemLink/SkylineCluster.ctl"/>
				<Item Name="SkylineCreate.vi" Type="VI" URL="../VIs/SystemLink/SkylineCreate.vi"/>
				<Item Name="SystemLink_RESTful.vi" Type="VI" URL="../VIs/SystemLink/SystemLink_RESTful.vi"/>
				<Item Name="SystemLinkHTTPComm.ctl" Type="VI" URL="../VIs/SystemLink/SystemLinkHTTPComm.ctl"/>
				<Item Name="TranslateTyping.vi" Type="VI" URL="../VIs/REPL/Subs/TranslateTyping.vi"/>
				<Item Name="WriteMultipleLines.vi" Type="VI" URL="../VIs/WriteMultipleLines.vi"/>
			</Item>
			<Item Name="vi.lib" Type="Folder">
				<Item Name="CFReleaseString.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/CFString.llb/CFReleaseString.vi"/>
				<Item Name="CFReleaseURL.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/CFURL.llb/CFReleaseURL.vi"/>
				<Item Name="CFStringCreate.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/CFString.llb/CFStringCreate.vi"/>
				<Item Name="CFStringGetCString.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/CFString.llb/CFStringGetCString.vi"/>
				<Item Name="CFStringGetLength.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/CFString.llb/CFStringGetLength.vi"/>
				<Item Name="CFStringRef.ctl" Type="VI" URL="/&lt;vilib&gt;/Platform/CFString.llb/CFStringRef.ctl"/>
				<Item Name="CFURLCopyFileSystemPath.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/CFURL.llb/CFURLCopyFileSystemPath.vi"/>
				<Item Name="CFURLCreateWithFileSystemPath.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/CFURL.llb/CFURLCreateWithFileSystemPath.vi"/>
				<Item Name="CFURLCreateWithString.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/CFURL.llb/CFURLCreateWithString.vi"/>
				<Item Name="CFURLRef.ctl" Type="VI" URL="/&lt;vilib&gt;/Platform/CFURL.llb/CFURLRef.ctl"/>
				<Item Name="Check if File or Folder Exists.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Check if File or Folder Exists.vi"/>
				<Item Name="Check Path.vi" Type="VI" URL="/&lt;vilib&gt;/picture/jpeg.llb/Check Path.vi"/>
				<Item Name="Compare Two Paths.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Compare Two Paths.vi"/>
				<Item Name="Dflt Data Dir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Dflt Data Dir.vi"/>
				<Item Name="Directory of Top Level VI.vi" Type="VI" URL="/&lt;vilib&gt;/picture/jpeg.llb/Directory of Top Level VI.vi"/>
				<Item Name="Draw Flattened Pixmap.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Draw Flattened Pixmap.vi"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Escape Characters for HTTP.vi" Type="VI" URL="/&lt;vilib&gt;/printing/PathToURL.llb/Escape Characters for HTTP.vi"/>
				<Item Name="eventvkey.ctl" Type="VI" URL="/&lt;vilib&gt;/event_ctls.llb/eventvkey.ctl"/>
				<Item Name="ex_CorrectErrorChain.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/ex_CorrectErrorChain.vi"/>
				<Item Name="FixBadRect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/pictutil.llb/FixBadRect.vi"/>
				<Item Name="Get File Extension.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Get File Extension.vi"/>
				<Item Name="imagedata.ctl" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/imagedata.ctl"/>
				<Item Name="InternetConfigLaunchURL.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/browser.llb/InternetConfigLaunchURL.vi"/>
				<Item Name="LabVIEWHTTPClient.lvlib" Type="Library" URL="/&lt;vilib&gt;/httpClient/LabVIEWHTTPClient.lvlib"/>
				<Item Name="List Directory and LLBs.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/List Directory and LLBs.vi"/>
				<Item Name="LVSelectionTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVSelectionTypeDef.ctl"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib"/>
				<Item Name="NI_PackedLibraryUtility.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/LVLibp/NI_PackedLibraryUtility.lvlib"/>
				<Item Name="Open URL in Default Browser (path).vi" Type="VI" URL="/&lt;vilib&gt;/Platform/browser.llb/Open URL in Default Browser (path).vi"/>
				<Item Name="Open URL in Default Browser (string).vi" Type="VI" URL="/&lt;vilib&gt;/Platform/browser.llb/Open URL in Default Browser (string).vi"/>
				<Item Name="Open URL in Default Browser core.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/browser.llb/Open URL in Default Browser core.vi"/>
				<Item Name="Open URL in Default Browser.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/browser.llb/Open URL in Default Browser.vi"/>
				<Item Name="Path To Command Line String.vi" Type="VI" URL="/&lt;vilib&gt;/AdvancedString/Path To Command Line String.vi"/>
				<Item Name="Path to URL.vi" Type="VI" URL="/&lt;vilib&gt;/printing/PathToURL.llb/Path to URL.vi"/>
				<Item Name="PathToUNIXPathString.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/CFURL.llb/PathToUNIXPathString.vi"/>
				<Item Name="Read JPEG File.vi" Type="VI" URL="/&lt;vilib&gt;/picture/jpeg.llb/Read JPEG File.vi"/>
				<Item Name="Recursive File List.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Recursive File List.vi"/>
				<Item Name="subFile Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/express/express input/FileDialogBlock.llb/subFile Dialog.vi"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="Version To Dotted String.vi" Type="VI" URL="/&lt;vilib&gt;/_xctls/Version To Dotted String.vi"/>
				<Item Name="VISA Configure Serial Port" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port"/>
				<Item Name="VISA Configure Serial Port (Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Instr).vi"/>
				<Item Name="VISA Configure Serial Port (Serial Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Serial Instr).vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
				<Item Name="XControlSupport.lvlib" Type="Library" URL="/&lt;vilib&gt;/_xctls/XControlSupport.lvlib"/>
			</Item>
			<Item Name="ApplicationServices.framework" Type="Document" URL="ApplicationServices.framework">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="Carbon.framework" Type="Document" URL="Carbon.framework">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="CoreFoundation.framework" Type="Document" URL="CoreFoundation.framework">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
