#!/home/woongsup/anaconda3/bin/python
import sys
import io
import cgi
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
import pandas as pd
from wordCloud import make_cloud
print("content-type: text/html; charset=utf-8\n")

df = pd.read_csv("./data/total_disease2_count_FINAL.csv", encoding="cp949")
df_10 = df.nlargest(10,'count')
name_list = list(df_10.loc[:, 'title'])
name_list.sort()
make_cloud()

print('''

<!DOCTYPE html>
  <html lang="en">
  <head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>어의가 없네</title>

    <!-- Custom fonts for this template-->
    <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">

    <!-- Custom styles for this template-->
    <link href="css/sb-admin-2.min.css" rel="stylesheet">

  </head>

  <body id="page-top">

    <!-- Page Wrapper -->
    <div id="wrapper">

      <!-- Sidebar -->
      <ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" id="accordionSidebar">

        <!-- Sidebar - Brand -->
        <a class="sidebar-brand d-flex align-items-center justify-content-center" href="index.py">
          <div class="sidebar-brand-icon rotate-n-15">
            <i class="fas fa-laugh-wink"></i>
          </div>
          <div class="sidebar-brand-text mx-3">어의가 없네</div>
        </a>

        <!-- Divider -->
        <hr class="sidebar-divider my-0">
    
        <!-- Heading -->
          <div class="sidebar-heading">
            Symptoms
          </div>
            <!-- Nav Item - Dashboard -->
          <li class="nav-item">
            <a class="nav-link" href="index.py">
              <i class="fas fa-fw fa-tachometer-alt"></i>
              <span>증상 입력</span></a>
          </li>
    
          <!-- Nav Item - Charts -->
          <li class="nav-item">
            <a class="nav-link" href="chart.py">
              <i class="fas fa-fw fa-chart-area"></i>
              <span>증상 예측</span></a>
          </li>
    
          <!-- Nav Item - Pages Collapse Menu -->
          <li class="nav-item">
            <a class="nav-link collapsed" href="banner.py">
              <i class="fas fa-fw fa-cog"></i>
              <span>증상 세부 설명</span></a>
          </li>
    
          <!-- Divider -->
          <hr class="sidebar-divider">
    
          <!-- Heading -->
          <div class="sidebar-heading">
            Data analysis
          </div>
    
    
          <li class="nav-item active">
            <a class="nav-link collapsed" href="usage.py">
              <i class="fas fa-fw fa-cog"></i>
              <span>사용자 이용 현황</span></a>
          </li>
    
          <li class="nav-item">
            <a class="nav-link collapsed" href="visual.py">
              <i class="fas fa-fw fa-cog"></i>
              <span>의료 데이터 시각화</span></a>
          </li>
    
          <li class="nav-item">
            <a class="nav-link collapsed" href="map.py">
              <i class="fas fa-fw fa-cog"></i>
              <span>근처 병원 안내</span></a>
          </li>
    
          <!-- Divider -->
          <hr class="sidebar-divider d-none d-md-block">

        <!-- Sidebar Toggler (Sidebar) -->
        <div class="text-center d-none d-md-inline">
          <button class="rounded-circle border-0" id="sidebarToggle"></button>
        </div>

      </ul>
      <!-- End of Sidebar -->


      <!-- Content Wrapper -->
      <div id="content-wrapper" class="d-flex flex-column">

        <!-- Main Content -->
        <div id="content">


          <!-- Begin Page Content -->
          <div class="container-fluid">

            <!-- Page Heading -->
            <h1 class="h3 mb-2 text-gray-800">사용자 이용 현황</h1>
            <p class="mb-4">사이트 이용자들의 데이터를 분석하여 시각화한 모습입니다.</a></p>




            <div class="row">

            <!-- Earnings (Monthly) Card Example -->
            <div class="col-xl-3 col-md-6 mb-4" id='banner1'>
              <button type="button" class="btn btn-outline-primary card border-left-primary shadow h-100 py-2 col mr-2">
                <div class="card-body">
                  <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                      <div class="font-weight-bold text-uppercase mb-1">가장 많이 검색된 병명</div>
                    </div>
                    <div class="col-auto">
                      <i class="fas fa-calendar fa-2x text-gray-300"></i>
                    </div>
                  </div>
                </div>
              </button>
            </div>

           

            <!-- Tasks Card Example -->
            <div class="col-xl-3 col-md-6 mb-4" id='banner3'>
             <!-- <button type="button" class="btn btn-outline-info card border-left-info shadow h-100 py-2 mr-2 col mr-2">
                <div class="card-body">
                  <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                      <div class="font-weight-bold text-uppercase mb-1">나이에 따른 병명 검색 순위</div>
                      <div class="row no-gutters align-items-center">
                        <div class="col-auto">
                        </div>
                      </div>
                    </div>
                    <div class="col-auto">
                      <i class="fas fa-clipboard-list fa-2x text-gray-300"></i>
                    </div>
                  </div>
                </div>
              </button> -->
            </div>

            <!-- Pending Requests Card Example -->
            <div class="col-xl-3 col-md-6 mb-4" id='banner4'>
              <button type="button" class="btn btn-outline-warning card border-left-warning shadow h-100 py-2 mr-2 col mr-2">
                <div class="card-body">
                  <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                      <div class="font-weight-bold text-uppercase mb-1">워드 클라우드</div>
                    </div>
                    <div class="col-auto">
                      <i class="fas fa-comments fa-2x text-gray-300"></i>
                    </div>
                  </div>
                </div>
              </div>
            </button>
          </div>




            <!-- Content Row -->
            <div class="row">

              <!-- Donut Chart -->
              <div class="col-xl-6 col-lg-5">
                <div class="card shadow mb-4">
                  <!-- Card Header - Dropdown -->
                  <div class="card-header py-3">
                    <span class="m-0 font-weight-bold text-primary" id="title1">가장 많이 검색된 병명</span>
                    <span style="float: right" class="m-0 font-weight-bold text-primary">(단위:건)</span>
                  </div>
                  <!-- Card Body -->
                  <div class="card-body">
                    <div class="chart-pie pt-4" id='content1'>
                        <canvas id="line-chart1"></canvas>
                    </div>

                    <hr>
                    <strong>사용자들이 가장 많이 검색한 병명 리스트입니다.</strong>
                  </div>
                </div>
              </div>

              <div class="col-xl-6 col-lg-5">
                <!-- Bar Chart -->
                <div class="card shadow mb-4">
                  <div class="card-header py-3">
                    <h6 class="m-0 font-weight-bold text-primary" id="title2">워드 클라우드</h6>
                  </div>
                  <div class="card-body">
                    <div class="chart-bar" id='content2'>
                         
                          <p><img src="./img/testwordcloud.png" width="600" height="350" id="img"></p>
                         
                         
                    </div>
                    <hr>
                    <strong>가장 많이 검색된 병명을 구름 모양으로 시각화한 모습입니다.</strong>
                  </div>
                </div>

              </div>

              
            </div>

          </div>
          <!-- /.container-fluid -->

        </div>
        <!-- End of Main Content -->
        
        
        <!-- Footer -->
        <footer class="sticky-footer bg-white">
          <div class="container my-auto">
            <div class="copyright text-center my-auto">
              <strong><span>(법적 한계에 대한 고지) </span></strong>
                <br><br>
                <strong><span>본 정보는 건강정보에 대한 소비자의 이해를 돕기 위한 참고자료일 뿐이며 <br> 개별 환자의 증상과 질병에 대한 정확한 판단을 위해서는 의사의 진료가 반드시 필요합니다.</span></strong>
            </div>
          </div>
        </footer>
        <!-- End of Footer -->

      </div>
      <!-- End of Content Wrapper -->

    </div>
    <!-- End of Page Wrapper -->

    <!-- Scroll to Top Button-->
    <a class="scroll-to-top rounded" href="#page-top">
      <i class="fas fa-angle-up"></i>
    </a>

    <!-- Logout Modal-->
    <div class="modal fade" id="logoutModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Ready to Leave?</h5>
            <button class="close" type="button" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">×</span>
            </button>
          </div>
          <div class="modal-body">Select "Logout" below if you are ready to end your current session.</div>
          <div class="modal-footer">
            <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
            <a class="btn btn-primary" href="login.html">Logout</a>
          </div>
        </div>
      </div>
    </div>

    <!-- Bootstrap core JavaScript-->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

    <!-- Core plugin JavaScript-->
    <script src="vendor/jquery-easing/jquery.easing.min.js"></script>

    <!-- Custom scripts for all pages-->
    <script src="js/sb-admin-2.min.js"></script>

    <!-- Page level plugins -->
    <script src="vendor/chart.js/Chart.min.js"></script>

    <!-- Page level custom scripts -->
    <script src="js/demo/chart-area-demo.js"></script>
    
    <script src="js/demo/chart-bar-demo.js"></script>
    <script type="text/javascript">
      var ctx = $("#line-chart1");
      var lineChart = new Chart(ctx, {
        type: 'bar',
        data: {
        ''')
print('''
          labels: {},
          '''.format(name_list))
print('''
          datasets: [
            {
              label: "",
              data: [10,8,6,5,12,8,16,17,6,7,6,10],
              backgroundColor: [ 
                        "rgba(242,166,54,.5)",
                        "rgba(39,79,76,.5)",
                        "rgba(40,161,130,.5)",
                        "rgba(206,29,22,.5)",
                        "rgba(242,166,54,.5)",
                        "rgba(39,79,76,.5)",
                        "rgba(40,161,130,.5)",
                        "rgba(206,29,22,.5)",
                        "rgba(242,166,54,.5)",
                        "rgba(39,79,76,.5)",
                        "rgba(40,161,130,.5)",
                        "rgba(206,29,22,.5)"
              ],
              borderColor: [
                       "rgb(242,166,54)",
                        "rgb(39,79,76)",
                        "rgb(40,161,130)",
                        "rgb(206,29,22)",
                        "rgb(242,166,54)",
                        "rgb(39,79,76)",
                        "rgb(40,161,130)",
                        "rgb(206,29,22)",
                        "rgb(242,166,54)",
                        "rgb(39,79,76)",
                        "rgb(40,161,130)",
                        "rgb(206,29,22)"
              ],
              hoverBackgroundColor:["rgb(242,166,54)",
                        "rgb(39,79,76)",
                        "rgb(40,161,130)",
                        "rgb(206,29,22)",
                        "rgb(242,166,54)",
                        "rgb(39,79,76)",
                        "rgb(40,161,130)",
                        "rgb(206,29,22)",
                        "rgb(242,166,54)",
                        "rgb(39,79,76)",
                        "rgb(40,161,130)",
                        "rgb(206,29,22)"],
              borderWidth: 1
            }
          ]
        },
        options: {
          maintainAspectRatio: false,
          legend:{
            display:false
          }
        }
      });
    </script>

    <script type="text/javascript">
      var ctx = $("#line-chart2");
      var lineChart = new Chart(ctx, {
        type: 'bar',
        data: {
        ''')
print('''
          labels: {},
          '''.format(name_list))
print('''
          datasets: [
            {
              label: "",
              data: [30,8,6,5,12,8,16,17,6,7,6,10],
              backgroundColor: [ 
                        "rgba(242,166,54,.5)",
                        "rgba(39,79,76,.5)",
                        "rgba(40,161,130,.5)",
                        "rgba(206,29,22,.5)",
                        "rgba(242,166,54,.5)",
                        "rgba(39,79,76,.5)",
                        "rgba(40,161,130,.5)",
                        "rgba(206,29,22,.5)",
                        "rgba(242,166,54,.5)",
                        "rgba(39,79,76,.5)",
                        "rgba(40,161,130,.5)",
                        "rgba(206,29,22,.5)"
              ],
              borderColor: [
                       "rgb(242,166,54)",
                        "rgb(39,79,76)",
                        "rgb(40,161,130)",
                        "rgb(206,29,22)",
                        "rgb(242,166,54)",
                        "rgb(39,79,76)",
                        "rgb(40,161,130)",
                        "rgb(206,29,22)",
                        "rgb(242,166,54)",
                        "rgb(39,79,76)",
                        "rgb(40,161,130)",
                        "rgb(206,29,22)"
              ],
              hoverBackgroundColor:["rgb(242,166,54)",
                        "rgb(39,79,76)",
                        "rgb(40,161,130)",
                        "rgb(206,29,22)",
                        "rgb(242,166,54)",
                        "rgb(39,79,76)",
                        "rgb(40,161,130)",
                        "rgb(206,29,22)",
                        "rgb(242,166,54)",
                        "rgb(39,79,76)",
                        "rgb(40,161,130)",
                        "rgb(206,29,22)"],
              borderWidth: 1
            }
          ]
        },
        options: {
          maintainAspectRatio: false,
          legend:{
            display:false
          }
        }
      });
    </script>

    
    
   
    
    
    
  </body>

  </html>



''')
