from django.shortcuts import render

# Create your views here.
def index(request):
    input_var=request.POST.get("input_var")
    if request.method=="POST":
        if input_var.lower().strip()=="home":
            home="""
            Hello There!
            I'm Saidur Rahman Siam
            An Intermediate Level Mobile App Developer
            
            First, Welcome to my portfolio. I think my portfolio may seem complicated to you and if so then please let me explain it to you.
            To access each section of my portfolio you have to enter the section name below like we do in terminal.
            Copy the section name from the menu and paste it or type it on the input section then press enter.
            That will open up the section you wants access.
            """
            sendvar={
                "page_body":home,
                }
            return render(request,"index.html",sendvar)
        elif input_var.lower().strip()=="about":
            about="""Saidur Rahman Siam
            Date of birth 6th June and current age 20(almost). Born and raised in Narsingdi, Dhaka, Bangladesh.
            Currently studing Diploma-in-Engineering on Computer Technology. Lead App Developer in Mangrove IT. CTO (Chief Technology officer) & Co-Founder of OneDream.
            """
            sendvar={
                "page_body":about,
                }
            return render(request,"index.html",sendvar)
        elif input_var.lower().strip()=="contact":
            contact="""For Email:
            sidurrahmansiam@gmail.com
            messagesiam@gmail.com
            
            Social Media Links:
            https://www.facebook.com/saidurrahmansiam007
            https://www.instagram.com/not_real_siam/
            https://github.com/Saltys-Git
            https://www.linkedin.com/in/saidur-rahman-siam
            https://www.g.dev/SaltysAppLab
            https://play.google.com/store/apps/dev?id=5482505048188819807
            """
            sendvar={
                "page_body":contact,
                }
            return render(request,"index.html",sendvar)
        elif input_var.lower().strip()=="skills":
            skills="""Started pursuing technology from the age of 9 and the first thing I tried out was photoshop on my brothers computer.
            The curiosity taught me HTML, Visual Basic, C, C#, Visual Effects, Music Compose, Cinematography and the last Mobile App Development(Java, Kotlin, Swift, Objective-C).
            """
            sendvar={
                "page_body":skills,
            }
            return render(request,"index.html",sendvar)
        elif input_var.lower().strip()=="projects":
            projects="""Personal Projects:
            Safe Youth App: An app to monitor automobile speed and maintain safety along with SOS feature.
            Rather Listen: An app to share your voice notes and audio books with others.
            
            Commersial Projects:
            Mangrove Smart Campus: An app with current userbase of 3000 students and 150+ teacher/stuffs to make campus life smarter and easier.
            OneDream: An app based on OneDream e-commerce bussinees to make accessibility more easier for its mobile users.
            """
            sendvar={
                "page_body":projects,
            }
            return render(request,"index.html",sendvar)
        else:
            comand=" were found"
            sendvar={
                "page_body":'error: no page named '+input_var+comand,
                }
            return render(request,"index.html",sendvar)
    sendvar={
            "page_body":"""
            Hello There!
            I'm Saidur Rahman Siam
            An Intermediate Level Mobile App Developer(Android & IOS)
            
            First, Welcome to my portfolio. I think my portfolio may seem complicated to you and if so then please let me explain it to you.
            To access each section of my portfolio you have to enter the section name below like we do in terminal.
            Copy the section name from the menu and paste it or type it on the input section then press enter.
            That will open up the section you wants access.
            """,
            }
    return render(request,"index.html",sendvar)