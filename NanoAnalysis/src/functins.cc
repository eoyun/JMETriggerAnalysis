#include "functions.h"

using namespace ROOT::VecOps;



ROOT::RDF::RNode RDFAddArray(ROOT::RDF::RNode df, ROOT::RVec<double> &v, const std::string &name) {
        return df.Define(name, [&](unsigned c) { return v[c]; }, {"counter"});
}
unsigned counter = 0;


vector<int> random_idx(){
    //std::cout<<std::rand()%2<<std::endl;

    vector<int> tnp;
    int tmp = std::rand()%2;

    tnp.push_back(tmp);
    tnp.push_back((tmp+1)%2);
    //std::cout<<tmp<< " | "<<(tmp+1)%2<<std::endl;
    return tnp;
}


double dphi(double phi1, double phi2){
    float x  = abs(phi1-phi2);
    if (x>M_PI)return 2*M_PI - x;
    else return x;
}


vector<int> match_hlt_offline ( ROOT::VecOps::RVec<float> hlt_eta,ROOT::VecOps::RVec<float> hlt_phi,ROOT::VecOps::RVec<float> off_eta,ROOT::VecOps::RVec<float> off_phi){
    vector<int> hlt_matched;
    int off_index;
    float dr=0.2;
    if  (off_eta.size()==0 || hlt_eta.size()==0) {
        hlt_matched.push_back(-1);
        return hlt_matched;
    }
    //for (int i=0; i< hlt_eta.size();i++){
    for (int i=0; i< off_eta.size();i++){
        off_index = -1;
        //std::cout<<off_phi.size()<<" | "<<off_eta.size()<<" | "<<i<<" | "<<hlt_phi.size()<<" | "<<hlt_eta.size()<<std::endl;
        for (int j=0;j<hlt_eta.size();j++){
            if (sqrt(pow(hlt_eta[j]-off_eta[i],2)+pow(hlt_phi[j]-off_phi[i],2))<dr){
                off_index = j;
                break;
            }
        }
        //std::cout<<off_index<<std::endl;
        hlt_matched.push_back(off_index);
    }
    //std::cout<<hlt_matched.size()<<" | "<<off_eta.size()<<" | "<<hlt_eta.size()<<std::endl;
    return hlt_matched;
}
